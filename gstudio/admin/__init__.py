"""Admin of Gstudio"""
from django.contrib import admin
from gstudio.models import Objecttype
from gstudio.models import Metatype
from gstudio.models import Relation
from gstudio.models import Relationtype
from gstudio.models import Attribute
from gstudio.models import Attributetype
from gstudio.models import System
from gstudio.models import Systemtype

from gstudio.admin.objecttype import ObjecttypeAdmin
from gstudio.admin.metatype import MetatypeAdmin
from gstudio.admin.relationtype import RelationtypeAdmin
from gstudio.admin.relation import RelationAdmin
from gstudio.admin.attribute import AttributeAdmin
from gstudio.admin.attributetype import AttributetypeAdmin
from gstudio.admin.system import SystemAdmin
from gstudio.admin.systemtype import SystemtypeAdmin


admin.site.register(Objecttype, ObjecttypeAdmin)

admin.site.register(Metatype, MetatypeAdmin)

admin.site.register(Relationtype, RelationtypeAdmin)
admin.site.register(Relation, RelationAdmin)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(Attributetype, AttributetypeAdmin)
admin.site.register(System, SystemAdmin)
admin.site.register(Systemtype, SystemtypeAdmin)


