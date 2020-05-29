from django.contrib.sessions.models import Session
from django.shortcuts import render,HttpResponse
from .models import admin
from .models import user_details
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import json
# Create your views here.
def index(request):
    return render(request,'index.html',{})
def about(request):
    return  render(request,'about.html')
def register(request):
    return render(request,'register.html')
def adminlogin(request):
    return render(request,'adminlogin.html')
def user(request):
    return render(request,'user.html')
def userhome(request):
    return render(request,'userhome.html')
def category_form(request):
    return render(request,'category_form.html')
def add_topics(request):
    return render(request,'add_topics.html')
def results(request):
    return render(request,'results.html')
def adminhome(request):
    return render(request,'adminhome.html')
def admin_add_topics(request):
    return render(request,'admin_add_topics.html')
def admin_analysis_result(request):
    return render(request,'admin_analysis_result.html')
def admin_login(request):
    username = request.POST.get('uname')
    password = request.POST.get('password')
    ad = admin.objects.all()
    for x in ad:
        if x.username == username and x.password == password:
            request.session['admin'] = x.username
            # user = authenticate(request, username=username, password=password)
            # login(request, user)
            return render(request, 'adminhome.html', {'uname': x.username})
    return render(request, 'adminlogin.html', {'msg': "Incorrect username or password.Try again"})


def admin_logout(request):
    # logout(request)
    # return render(request, 'home.html')

    try:
        ss = Session.objects.all().delete()
        ss.save()
        request.session['admin'].delete()
        del request.session['password']
    except:
        pass
        return render(request, 'adminlogin.html')


def user_reg(request):
    db = user_details(Name=request.POST.get('name'),
                      Dob=request.POST.get('date'), Gender=request.POST.get('gender'),
                      Mobile=request.POST.get('mobile'),email=request.POST.get('email'),
                      username=request.POST.get('uname'), password=request.POST.get('password'))

    db.save()
    return render(request, 'register.html', {'msg': "Successfully Inserted"})

def user_login(request):
    username = request.POST.get('uname')
    password = request.POST.get('password')
    ad = user_details.objects.all()
    for x in ad:
        if x.username == username and x.password == password:
            request.session['user'] = x.username
            # user = authenticate(request, username=username, password=password)
            # login(request, user)
            return render(request, 'userhome.html', {'uname': x.username})
    return render(request, 'user.html', {'msg': "Incorrect username or password.Try again"})


def user_logout(request):
    # logout(request)
    # return render(request, 'home.html')

    try:
        ss = Session.objects.all().delete()
        ss.save()
        request.session['user'].delete()
        del request.session['password']
    except:
        pass
        return render(request, 'user.html')


#def our_posts(request):
    
    ##with open('file.php') as f:
     #data1 = json.load(f)
     #data2 = json.dumps(data1)
     #return render(request, 'our_posts.html', {'value':data2})

def testCode(request):
    import pymysql
    from django.http import JsonResponse
    db = pymysql.connect("localhost", "root", "", "socialdb")
    cursor = db.cursor()

    sql = "select * from post LEFT JOIN members on members.member_id = post.member_id"


    posts=[]
    try:
        # Execute the SQL command
        cursor.execute(sql)

        results = cursor.fetchall()

        i=0
        for row in results:
            tempPost={}
            tempPost['post_id']=row[0]
            tempPost['member_id']=row[1]
            tempPost['content']=row[2]
            tempPost['date_posted']=row[3]
            tempPost['firstname']=row[5]
            tempPost['lastname']=row[6]
            tempPost['middlename']=row[7]
            tempPost['address']=row[8]
            tempPost['email']=row[9]
            tempPost['contact_no']=row[10]
            tempPost['age']=row[11]
            tempPost['gender']=row[12]
            tempPost['username']=row[13]
            tempPost['password']=row[14]
            tempPost['image']=row[15]
            tempPost['birthdate']=row[16]
            tempPost['mobile']=row[17]
            tempPost['status']=row[18]
            tempPost['work']=row[19]
            tempPost['religion']=row[19]

            #tempPost['sentiment']=sentiment_analyser(row[2])
            posts.append(tempPost)
        #print(posts)


        # Commit your changes in the database
        db.commit()
    except Exception as e:
        # Rollback in case there is any error
        print(e)
        db.rollback()
    return JsonResponse(posts, safe=False)
    db.close()


def admin_posts(request):
    return render(request,'admin_posts.html')

def user_posts(request):
    return render(request,'my_posts.html')


def view_users(request):
    users = user_details.objects.all()
    return render(request, 'view_users.html', {'users': users})

def analysis(request):
    import pymysql
    from django.http import JsonResponse
    db = pymysql.connect("localhost", "root", "", "socialdb")
    cursor = db.cursor()
    p_id = request.GET.get('p_id')

    print(p_id)
    sql = "SELECT `comment`.*,`post`.* FROM `comment` LEFT JOIN `post` ON `comment`.`p_id`=`post`.`post_id` WHERE `comment`.`p_id`='%s'"%p_id

    comments = []
    try:
        # Execute the SQL command
        cursor.execute(sql)

        results = cursor.fetchall()

        i=0
        for row in results:
            tempComment={}

            tempComment['id']=row[0]
            tempComment['p_id']=row[1]
            tempComment['comment']=row[3]
            tempComment['date']=row[4]
            tempComment['analysis']=sentiment_analyser(row[3])
            comments.append(tempComment)
        #print(posts)


        # Commit your changes in the database
        db.commit()
    except Exception as e:
        # Rollback in case there is any error
        print(e)
        db.rollback()
    return JsonResponse(comments, safe=False)
    db.close()

    #return render(request,'analysis.html')

def view_comments(request):
    return render(request,'analysis.html')
def comments(request):
    return render(request,'comments.html')


#logic
def sentiment_analyser(plain_text):
    response = (get_text_sentiment(plain_text))
    return response



def log_error(e):
    print(e)


# Sentiment analysis
def clean_text(tweet):
    '''
    Utility function to clean text by removing links, special characters
    using simple regex statements.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\S+)", " ", tweet).split())


def get_text_sentiment(text):
    '''
    Utility function to classify sentiment of passed tweet
    using textblob's sentiment method
    '''
    # create TextBlob object of passed tweet text
    analysis = TextBlob(clean_text(text))
    # set sentiment
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

def values(request):
    u_name = request.session['user']
    import pymysql
    from django.http import JsonResponse
    db = pymysql.connect("localhost", "root", "", "socialdb")
    cursor = db.cursor()
    qr = "select member_id from members where username='%s'"%u_name
    cursor.execute(qr)
    results=cursor.fetchall()
    for row in results:
        m_id=row[0]
    sql = "select * from post LEFT JOIN members on members.member_id = post.member_id where members.member_id='%s'"%m_id
    #print(sql)
    posts = []
    try:
        # Execute the SQL command
        cursor.execute(sql)

        results = cursor.fetchall()

        i = 0
        for row in results:
            tempPost = {}
            tempPost['post_id'] = row[0]
            tempPost['member_id'] = row[1]
            tempPost['content'] = row[2]
            tempPost['date'] = row[3]

            # tempPost['sentiment']=sentiment_analyser(row[2])
            posts.append(tempPost)
        # print(posts)

        # Commit your changes in the database
        db.commit()
    except Exception as e:
        # Rollback in case there is any error
        print(e)
        db.rollback()
    return JsonResponse(posts, safe=False)
    db.close()

def our(request):
    import pymysql
    from django.http import JsonResponse
    db = pymysql.connect("localhost", "root", "", "socialdb")
    cursor = db.cursor()
    p_id = request.GET.get('p_id')

    print(p_id)
    sql = "SELECT `comment`.*,`post`.* FROM `comment` LEFT JOIN `post` ON `comment`.`p_id`=`post`.`post_id` WHERE `comment`.`p_id`='%s'" % p_id

    comments = []
    try:
        # Execute the SQL command
        cursor.execute(sql)

        results = cursor.fetchall()

        i = 0
        for row in results:
            tempComment = {}

            tempComment['id'] = row[0]
            tempComment['p_id'] = row[1]
            tempComment['comment'] = row[3]
            tempComment['date'] = row[4]
            tempComment['analysis'] = sentiment_analyser(row[3])
            comments.append(tempComment)
        # print(posts)

        # Commit your changes in the database
        db.commit()
    except Exception as e:
        # Rollback in case there is any error
        print(e)
        db.rollback()
    return JsonResponse(comments, safe=False)
    db.close()

