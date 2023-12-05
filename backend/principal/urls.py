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
    path('cargarPaginas/<str:dia>/<str:mes>/<str:año>', views.cargarPaginas, name='cargarPaginas'),
    path('cargarGanancia/', views.cargarDataUnidad, name='cargarData'),
    path('selenium/', views.selenium, name='selenium'),
    path('asignarPagina/', views.asignarPagina, name='AsignarPagina'),
    path('chaturbate/', views.chaturbate, name='Chaturbate'),
    path('stripchat/', views.stripchat, name='Stripchat'),
    path('bonga/', views.bonga, name='Bonga'),
    path('flirt4free/', views.flirt4free, name='Flirt4free'),
    path('streamate/', views.streamate, name='Streamate'),
    path('jasmin/', views.jasmin, name='Jasmin'),
    path('imlive/', views.imlive, name='Imlive'),
    # Incluye las rutas del router
    path('', include(router.urls)),
]