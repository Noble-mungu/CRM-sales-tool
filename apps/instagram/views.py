from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def instagramView(request):
    return render(request,'common/instagram.html')

@login_required(login_url='/login')
def personal_profile(request):
    if request.method == 'POST' and request.FILES.get('profile'):
        profile_image = request.FILES.get('profile')
        user = request.user
        profile = Profile(user=user,profile_image = profile_image)
        profile.save()
        user.profile = profile
        user.save()

    # posts = Post.get_posts_for_user(request.user.id)
    # post_count = len(post)
    return render(request,'common/personal-profile.html')


@login_required(login_url='/login')
def competitors_profile(request):
    if request.method == 'POST' and request.FILES.get('profile'):
        profile_image = request.FILES.get('profile')
        user = request.user
        profile = Profile(user=user,profile_image = profile_image)
        profile.save()
        user.profile = profile
        user.save()
    return render(request,'common/competitors-profile.html')
@login_required(login_url='/login')
def upload_pic(request):
    if request.method == 'POST':
        if request.FILES.get('upload'):
            post_image = request.FILES.get('upload')
            post_description = request.POST.get('description')

            user = request.user
            post = Post(user = user, post_description = post_description, post_image = post_image)
            post.save()
            user.post = post
            user.save()
            return redirect('common/personal-profile.html')
        else:
            return render(request, 'common/upload.html', {'error': 'Make sure you select an image'})
    else:
        return render(request, 'common/upload.html')
def show_post(required,post_id):
    post = Post.object.get(id = post_id)
    comments = list(Comment.object.filter(post=post))
    print(comment)
    return render(request,'common/post.html',{'post':post,'comments':comments})
@login_required(login_url='/login')
def like_post(request):
    if request.method =='POST':
        if request.POST.get('like'):
            post_id = int(request.POST.get('like'))
            if isinstance(post_id, int):
                print(post_id)
                post_to_like = Post.objects.get(id = post_id)
                like_post = Like(username=request.user.username)
                like_post.save()
                like_post.post.add(post_to_like)
                data = {'success': 'Successfully liked the post'}
                return JsonResponse(data)
            else:
                data = {'fail': 'Something wrong happened.'}
                return JsonResponse(data)


@login_required(login_url='/login')
def make_comment(request):
    if request.method =='POST':
        if request.POST.get('comment'):
            post_id = int(request.POST.get('post'))
            comment = request.POST.get('comment')
        elif request.POST.get('comment-lg'):
            post_id = int(request.POST.get('post-lg'))
            comment = request.POST.get('comment-lg')
        else:
            data = {'fail': 'Something wrong happened.'}
            return JsonResponse(data)

        if isinstance(post_id, int):
            print(post_id)
            print(comment)
            post_to_comment = Post.objects.get(id = post_id)
            comment_post = Comment(username=request.user.username, comment = comment)
            comment_post.save()
            comment_post.post.add(post_to_comment)
            profile = Profile.objects.filter(user=request.user.id).exists()
            if profile:
                comment = {'user': request.user.username,'image': request.user.profile.profile_image.url, 'comment': comment}
            else:
                comment = {'user': request.user.username,'image': None, 'comment': comment}
            data = {'success': 'Successfully liked the post', 'comment': comment}
            return JsonResponse(data)
        else:
            data = {'fail': 'Something wrong happened.'}
            return JsonResponse(data)
