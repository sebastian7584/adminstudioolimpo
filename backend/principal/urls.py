from django.urls import path
from . import viewsets
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

urlpatterns = router.urls