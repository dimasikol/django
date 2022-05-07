from django.shortcuts import render,redirect
from django.views import generic
from django.http import HttpResponseRedirect
from ..logicquiz import task1
from ..models.quiz_result_student import QuizResult
import random
import time
class ShowQuizView(generic.View):
    def get(self,request,**kwargs):
        d=time.time()
        self.context1=[random.choice([task1.Task1().write1(),task1.Task1().write2(),task1.Task1().write3()]) for _ in range(int(kwargs['id']))]




        self.context7=[task1.Task7().write() for _ in range(int(kwargs["id"]))]
        self.context8=[task1.Task8().write() for _ in range(int(kwargs["id"]))]
        self.context10=[random.choice([task1.Task10().write1()]) for _ in range(int(kwargs['id']))]
        print(time.time()-d)
        context = {"context1": self.context1, "context8": self.context8,"context7":self.context7 , "context10": self.context10}
        return render(request,"bShop/template_randomaize_quiz_generation/base.html",context=context)

    def post(self,request,**kwargs):
        if request.method=='POST': #and str(request.user)!="AnonymousUser":
            base_date=QuizResult(answer=request.POST,student=request.user,question_number="answer1",question_type='oge',result=0)
            base_date.save()
            return render(request,"bShop/template_randomaize_quiz_generation/quiz/quiz_result.html")

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))