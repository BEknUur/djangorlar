from django.urls import path,include 
from rest_framework.routers import DefaultRouter
from apps.education.views import CourseViewSert,LessonViewSet

router:DefaultRouter=DefaultRouter(trailig_slash=False)
router.register(prefix="courses",viewset=CourseViewSert,basename="courses")
router.register(prefix="lessons",viewset=LessonViewSet,basename="lessons")

urlpatterns=[
    path("v1",include(router.urls))
]