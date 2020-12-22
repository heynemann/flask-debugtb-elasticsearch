# Flask DebugToolbar Panel for ElasticSearch Queries

## DISCLAIMER

This project is HEAVILY based on the work by @bobosss on his flask_debugtoolbar_elasticsearch. I just fixed a few things
and packaged it properly to use in pypi.

## Installing

    $ pip install flask-debugtb-elasticsearch

## Usage

Just include in your panels:

    app.config['DEBUG_TB_PANELS'].append('flask_debugtb_elasticsearch.panel.ElasticsearchDebugPanel')
    
Or:

    app.config["DEBUG_TB_PANELS"] = list(app.config["DEBUG_TB_PANELS"])
    app.config["DEBUG_TB_PANELS"].append('flask_debugtb_elasticsearch.panel.ElasticsearchDebugPanel')

And that's all there is to it.

## Contributing

Fork, PR, Rinse and Repeat.

## Licensing

The MIT License (MIT)

Copyright (c) 2015 Bernardo Heynemann

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
