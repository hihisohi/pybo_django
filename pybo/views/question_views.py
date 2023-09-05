from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question

@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)  # 임시 저장하여 question 객체를 리턴
            question.author = request.user
            question.create_date = timezone.now()   # 실제 저장을 위해 작성일시를 설정 (데이터 저장 시점에 생성해야 하는 값이므로 QuestionForm에 등록하여 사용하지 않음)
            question.save() # 데이터를 실제로 저장
            return redirect('pybo:index')
    else:
        form = QuestionForm()
        
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정 권한이 없습니다.')    # 넌필드 오류(non-field error) 발생
        return redirect('pybo:detail', question_id=question.id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)    #  instance를 기준으로 QuestionForm을 생성하지만 request.POST의 값으로 덮어쓰라는 의미
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)  # instance 값을 지정하면 폼의 속성 값이 instance의 값으로 채워짐
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')

@login_required(login_url='common:login')
def question_vote(requset, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if requset.user == question.author:
        messages.error(requset, '본인이 작성한 글은 추천할 수 없습니다.')
    else:
        question.voter.add(requset.user)    # 여러사람을 추가할 수 있는 ManyToManyField이므로 add 함수를 사용
        # 동일한 사용자가 동일한 질문을 여러번 추천하더라도 추천수 증가 X, 오류 X
        # ===> ManyToManyField 내부에서 자체적으로 처리
    return redirect('pybo:detail', question_id=question.id)