#!/usr/bin/env python
# coding:utf-8
from _base.config import Config
from bson.objectid import ObjectId
from mongokit import Document, Connection
from mongokit.document import DocumentProperties
import mongokit.connection


mongo = Connection(**Config.MONGO)


class MetaDoc(DocumentProperties):

    def __new__(cls, name, bases, attrs):
        new_cls = super(MetaDoc, cls).__new__(cls, name, bases, attrs)
        if bases[0] is not Document:

            new_cls.__mongo__ = mongo
            if not new_cls.__name__.startswith('Callable'):
                new_cls.__collection__ = (name[0].lower() + name[1:])
                new_cls = mongo.register(new_cls)
                new_cls = getattr(mongo, name)
            else:
                new_cls._protected_field_names.append("_collection")
                _ = getattr(new_cls.__mongo__, new_cls.__database__)
                _ = getattr(_, new_cls.__collection__)
                new_cls._collection = _

        return new_cls


class Doc(Document):
    __metaclass__ = MetaDoc
    __database__ = Config.APP
    use_dot_notation = True
    use_autorefs = False
    skip_validation = True

    def __init__(self, doc={}, gen_skel=False, *args, **kwds):
        if doc is None:
            doc = {}
        super(Doc, self).__init__(doc, *args, **kwds)
        for i in self.structure:
            if i not in doc:  # 没初始化的记录设为None
                self[i] = None

        if gen_skel:  # 设置默认值
            if self.default_values:
                self._set_default_fields(self, self.structure)

    def upsert(self, spec):
        if isinstance(spec, basestring):
            spec = {'_id': ObjectId(spec)}

        self.collection.update(
            spec,
            {'$set': dict((k, v) for k, v in self.iteritems() if v is not None)},
            upsert=True
        )
        return self

    def save(self, *args, **kwds):
        if "_id" in self:
            _id = self['_id']
            if isinstance(_id, basestring):
                self['_id'] = ObjectId(_id)
        super(Doc, self).save(*args, **kwds)
        return self

    @classmethod
    def update(cls, *args, **kwds):
        return cls._collection.update(*args, **kwds)

    @classmethod
    def count(cls, *args, **kwds):
        return cls._collection.find(*args, **kwds).count()

    @classmethod
    def find(cls, *args, **kwds):
        result = []
        for i in cls._collection.find(*args, **kwds):
            i['_id'] = str(i['_id'])
            result.append(i)
        return map(lambda doc: cls(doc, collection=cls._collection), result)

    @classmethod
    def find_one(cls, spec_or_id=None, create_new=False, *args, **kwds):
        if isinstance(spec_or_id, basestring):
            spec_or_id = ObjectId(spec_or_id)
        o = cls._collection.find_one(spec_or_id, *args, **kwds)
        if o:
            o['_id'] = str(o['_id'])
            return cls(o, collection=cls._collection)
        elif create_new == True:
            return cls({}, collection=cls._collection)

    def delete(self):
        self._collection.remove({'_id': ObjectId(self['_id'])})

    @classmethod
    def remove(cls, spec_or_id=None, safe=None, multi=True, **kwargs):
        if isinstance(spec_or_id, basestring):
            spec_or_id = ObjectId(spec_or_id)
        cls._collection.remove(spec_or_id=spec_or_id, safe=safe, multi=multi, **kwargs)


class CallableMixin(object):

    """重写参数gen_skel的默认值为False.

    若为 True, 查询时得到的纪录值会被 default_values 里的值覆盖
    """

    def __call__(self, doc=None, gen_skel=False, lang='en', fallback_lang='en'):
        return self._obj_class(
            doc=doc,
            gen_skel=gen_skel,
            collection=self.collection,
            lang=lang,
            fallback_lang=fallback_lang
        )
mongokit.connection.CallableMixin = CallableMixin
