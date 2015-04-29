from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

class CMSTestApphook(CMSApp):
    name = "CMS Test Apphook"
    urls = ['cmstest.urls']

apphook_pool.register(CMSTestApphook)
