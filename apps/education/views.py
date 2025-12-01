from django.shortcuts import render
from django.db.models import Count

from rest_framework.response import Response
from rest_framework.viewsets import ViewSet 
from rest_framework.request import Request 
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_201_CREATED,
    HTTP_403_FORBIDDEN
)
from rest_framework.decorators import action 
from rest_framework.permissions import IsAuthenticated,AllowAny

from apps.education.models import Course
from apps.education.serializers import CouseSeralizer,LessonSeralizer
from apps.education.permissions import IsCourseOwner,IsOwner

class CourseViewSert(ViewSet):
    """
    VIew set for managing
    """
    permission_classes=(IsAuthenticated,IsOwner)

    def get_seralizer(self,*args,**kwargs):
        seralizer_class=self.get_seriliser_class()
        if seralizer_class:
            kwargs.setdefault("context",{"request":self.request,"view":self})
            return seralizer_class(*args,**kwargs)
        return None 
    
    def list(self,request:Request,*args,**kwargs)->Response:
        course=Course.objects.all()
        is_active=request.query_params.get("is_active")
        if is_active:
            course=course.filter(is_active=is_active.lower()=="true")

        courses=courses.annotate(lessons_count=Count("lessons"))

        seralizer=CouseSeralizer(courses,many=True)
        return Response(seralizer.data,status=HTTP_200_OK)
    
    def create(self,request:Request)->Response:
        seralizer=CouseSeralizer(data=request.data)
        if seralizer.is_valid():
            seralizer.save(owner=request.user)
            return Response(seralizer.data,status=HTTP_201_CREATED)
        return Response(seralizer.errors,status=HTTP_400_BAD_REQUEST)
    

    def retrieve(self,request:Request,pk:int)->Response:
        try:
            course=Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response({"detail":"course not found"},status=HTTP_404_NOT_FOUND)
        

    def update(self,request:Request,pk:int)->Response:
        try:
            course=Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response({"detail":"course not found"},status=HTTP_404_NOT_FOUND)
        
        self.check_object_permissions(request,course)
        if serializer.is_valid():
            seralizer.save()
            return Response(seralizer.data,status=HTTP_200_OK)
        return Response(seralizer.errors,status=HTTP_400_BAD_REQUEST)
    

    def destroy(self,request:Request,pk:int)->Response:
        try:
            course=Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response({"detail":"course not found"},status=HTTP_404_NOT_FOUND)
        self.check_object_permissions(request,course)
        course.delete()
        return Response(status=HTTP_200_OK)
    
    @action(
        methods=["post"],
        detail=True,
        permission_classes=[IsAuthenticated,IsCourseOwner]

    )
    def activate(self,request:Request,pk:int)->Response:
        try:
            course=Course.objects.get(pk=pk)
        
        except Course.DoesNotExist:
            return Response({"detail":"course not found"},status=HTTP_404_NOT_FOUND)
        self.check_object_permissions(request,course)
        course.is_active=True
        course.save()
        seralizer=CouseSeralizer(course)
        return Response(seralizer.data,status=HTTP_200_OK)
    @action(
        methods=["post"],
        detail=True,
        permission_classes=[IsAuthenticated,IsCourseOwner],
    )
    
    def deactivate(self,request:Request,pk:int)->Response:
        try:
            course=Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response({"detail":"course not found"},status=HTTP_404_NOT_FOUND)
        self.check_object_permissions(request,course)
        course.is_active=False
        course.save()
        seralizer=CouseSeralizer(course)
        return Response(seralizer.data,status=HTTP_200_OK)  
    
    @action(
        methods=["get"],
        permission_classes=[AllowAny],
        detail=True,
    )
    def lessons(self,request:Request,pk:int)->Response:
        try:
            course=Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response({"detail":"course not found"},status=HTTP_404_NOT_FOUND)
        lessons=Lesson.objects.filter(course=course)
        seralizer=LessonSeralizer(lessons,many=True)
        return Response(seralizer.data,status=HTTP_200_OK)

    

class LessonViewSet(ViewSet):
    """
    ViewSet for managing lessons
    """
    permission_classes=(IsAuthenticated,IsOwner)

def get_seralizer_class(self):
    return LessonSeralizer

def get_seralizer(self,*args,**kwargs):
    seralizer_class=self.get_seralizer_class()
    if seralizer_class:
        kwargs.setdefault("context",{"request":self.request,"view":self})
        return seralizer_class(*args,**kwargs)
    return None 
def crete(self,request:Request)->Response:
    course_id=request.data.get("course")
    course=Course.objects.filter(id=course_id).first()
    if not course:
        return Response({"detail":"course not found"},status=HTTP_404_NOT_FOUND)
    
    self.check_object_permissions(request,course)
    first=Lesson.object.filter(course=course).order_by("order").first()
    order=first.order -1 if first else 1 
    seralizer=LessonSeralizer(data=request.data)
    if seralizer.is_valid():
        seralizer.save(course=course,order=order)
        return Response(seralizer.data,status=HTTP_201_CREATED)
    return Response(seralizer.errors,status=HTTP_400_BAD_REQUEST)
@action(
    methods=["post"],
    detail=True,
)
def move(self,request:Request,pk:int)->Response:
    try:
        lesson=Lesson.objects.get(pk=pk)
    except Lesson.DoesNotExist:
        return Response({"detail":"lesson not found"},status=HTTP_404_NOT_FOUND)
    self.check_object_permissions(request,lesson.course)
    before_id=request.data.get("before_lesson_id")
    if before_id:
        before=Lesson.objects.filter(pk=before_id).first()
        if before:
            lesson.order=before.order -1 

    else:
        last=(
            Lesson.objects.filter(course=lesson.course)
            .order_by("order")
            .last()
        
        )    
        lesson.order=(last.order+1) if last else 1 

        lesson.save()
        seralizer=LessonSeralizer(lesson)
        return Response(seralizer.data,status=HTTP_200_OK)
    

  def destroy(self, request: Request, pk: int) -> Response:
        try:
            lesson = Lesson.objects.get(pk=pk)
        except Lesson.DoesNotExist:
            return Response({"detail": "Lesson not found."}, status=HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, lesson.course)

        lesson.delete()
        return Response(status=HTTP_200_OK)

    @action(
        methods=["post"],
        # FIX: Removed AllowAny to enforce authentication and ownership
        detail=True,
    )
    def publish(self, request: Request, pk: int) -> Response:
        try:
            lesson = Lesson.objects.get(pk=pk)
        except Lesson.DoesNotExist:
            return Response({"detial": "Lesson not found."}, status=HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, lesson.course)

        lesson.is_published = True
        lesson.save()
        serializer = LessonSerializer(lesson)
        return Response(serializer.data, status=HTTP_200_OK)

    @action(
        methods=["post"],
        # FIX: Removed AllowAny
        detail=True,
    )
    def unpublish(self, request: Request, pk: int) -> Response:
        try:
            lesson = Lesson.objects.get(pk=pk)
        except Lesson.DoesNotExist:
            return Response({"detial": "Lesson not found."}, status=HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, lesson.course)

        lesson.is_published = False
        lesson.save()
        serializer = LessonSerializer(lesson)
        return Response(serializer.data, status=HTTP_200_OK)