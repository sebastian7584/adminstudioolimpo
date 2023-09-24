from django.urls import path, include
from . import viewsets
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register('country', viewsets.CountryViewSet)
router.register('bank', viewsets.BankViewSet)
router.register('user', viewsets.UserViewSet)
router.register('typepage', viewsets.TypePageViewSet)
router.register('page', viewsets.PageViewSet)
router.register('payment', viewsets.PaymentViewSet)
router.register('owner', viewsets.OwnerViewSet)
router.register('master', viewsets.MasterViewSet)
router.register('account', viewsets.AccountViewSet)
router.register('period', viewsets.PeriodViewSet)
router.register('earning', viewsets.EarningViewSet)
router.register('document', viewsets.DocumentViewSet)
router.register('advance', viewsets.AdvanceViewSet)


urlpatterns = [
    # Rutas para funciones de vista normales
    path('cargarChaturbate/<str:dia>/<str:mes>/<str:año>/<str:save>', views.cargarChaturbate, name='cargarChaturbate'),
    path('cargarStripchat/<str:dia>/<str:mes>/<str:año>/<str:save>', views.cargarStripchat, name='cargarStripchat'),
    
    # Incluye las rutas del router
    path('', include(router.urls)),
]