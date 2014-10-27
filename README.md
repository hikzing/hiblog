### A Clean And Pure Blog

**which Powered by [Tornado][1] and [clean-blog][2] theme**


### Features:

* Admin manager
* Message System
* Markdown syntax

### Requirements
>
1. [Tornado][1]
2. [Mongo][3]
3. [Redis][4]

### Setup

1. get source code: `git clone https://github.com/Kzinglzy/hiblog`

2. Install required package: `pip install -r requirements.txt`

3. edit the `hiblog/_base/config.py` & `hiblog/_base/setting.py` for personal
setting.

4. run `python tools/admin_guide.py` to create a admin user

5. run `python tools/run.py` to start the blog server

> For more details and develop suggestions, see [Here][5](CN)

### Licence

MIT Licence. See MIT-LICENCE


[1]: http://www.tornadoweb.org/
[2]: https://github.com/ironsummitmedia/startbootstrap-clean-blog/
[3]: https://www.mongodb.org
[4]: https://redis.io
[5]: http://kzing.net/blog/关于这个blog
