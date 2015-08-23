#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of flask-debugtb-elasticsearch.
# https://github.com/heynemann/flask-debugtb-elasticsearch

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Bernardo Heynemann <heynemann@gmail.com>


import json
import jinja2
from flask_debugtoolbar.panels import DebugPanel
from flask_debugtoolbar_elasticSearch.utils import ThreadCollector

from elasticsearch.connection.base import Connection


collector = ThreadCollector()


old_log_request_success = Connection.log_request_success

_ = lambda x: x


def patched_log_request_success(self, method, full_url, path, body, status_code, response, duration):
    collector.collect(ElasticQueryInfo(method, full_url, path, body, status_code, response, duration))
    old_log_request_success(self, method, full_url, path, body, status_code, response, duration)

Connection.log_request_success = patched_log_request_success


def _pretty_json(data):
    # pretty JSON in tracer curl logs
    try:
        return json.dumps(json.loads(data), sort_keys=True, indent=2, separators=(',', ': ')).replace("'", r'\u0027')
    except (ValueError, TypeError):
        # non-json data or a bulk request
        return data


class ElasticQueryInfo():
    def __init__(self, method, full_url, path, body, status_code, response, duration):
        self.method = method
        self.full_url = full_url
        self.path = path
        self.body = _pretty_json(body)
        self.status_code = status_code
        self.response = _pretty_json(response)
        self.duration = round(duration * 1000, 2)


class ElasticsearchDebugPanel(DebugPanel):
    name = 'Elastic'
    has_content = True
    records = []

    def __init__(self, *args, **kwargs):
        super(ElasticsearchDebugPanel, self).__init__(*args, **kwargs)
        self.jinja_env.loader = jinja2.ChoiceLoader([
            self.jinja_env.loader,
            jinja2.PrefixLoader({
                'debug_tb_elastic': jinja2.PackageLoader(__name__, 'templates')
            })
        ])

    def nav_title(self):
        return _('Elastic Queries')

    def nav_subtitle(self):
        return "{} queries {}ms".format(self.nb_queries, self.total_time)

    def title(self):
        return _('Elastic')

    def process_request(self, request):
        collector.clear_collection()

    def url(self):
        return ''

    def process_response(self, request, response):
        records = collector.get_collection()
        self.total_time = 0

        for record in records:
            self.total_time += record.duration

        self.nb_queries = len(records)

        collector.clear_collection()
        self.records = records

    def content(self):
        context = self.context.copy()
        context.update({
            'records': self.records,
            'debug': True,
        })

        return self.render('debug_tb_elastic/elasticsearch.html', context)
