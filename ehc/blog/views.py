import spacy
from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")

# Create a new instance of the ChatBot class
bot = ChatBot(
    'chatbot',
    read_only=False,
    tagger_language=nlp  # Pass the SpaCy language model instance

)
# Define a list of conversational pairs to train the chatbot
list_to_train = [
    "hi",
    "hi, there",
    "What's your name?",
    "EHC Chatbot",
    "i have a problem with my hardware",
    "okay tell me more details about your problem",
    "i have an overheat on my laptop",
    "try to put your laptop in low tempreature place or on an table of glass",
   

]

# Train the chatbot using ChatterBotCorpusTrainer
chatterBotCorpusTrainer = ChatterBotCorpusTrainer(bot)
chatterBotCorpusTrainer.train('chatterbot.corpus.english')

# Define the index view function
def index(request):
    return render(request, 'blog/chatbot.html')

# Define the specific view function
def specific(request):
    number = 55
    return HttpResponse(number)

# Define the getResponse view function
def getResponse(request):
    if request.method == 'GET':
        # Get the user message from the request parameters
        user_message = request.GET.get('userMessage', '')

        # Get the response from the chatbot
        chat_response = str(bot.get_response(user_message))

        # Return the response as an HTTP response
        return HttpResponse(chat_response)
    else:
        # If the request method is not GET, return a method not allowed response
        return HttpResponse(status=405)



from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import   *
from .models import  *
from django.shortcuts import render, redirect




def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['PhoneNumber']

            # Create a new SiteUser instance
            user = SiteUser(username=username, password=password, Email=email, PhoneNumber=phone_number)
            user.save()

            return redirect('login')  # Redirect to a success page
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    error_message = 'Invalid username or password. Please try again.'
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = SiteUser.objects.filter(username=username, password=password).first()
            if user:
                # set user session
                request.session['user_id'] = user.id
                return redirect('select')
            else:
                # invalid login
                return render(request, 'registration/login.html', {'form': form, 'error_message': error_message})
    else:
        form = LogInForm()
        return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('login')  # Redirect to the login page after logout



def CreateTicket(request):
    user_id = request.session.get('user_id')
    user = SiteUser.objects.get(id=user_id)
    success_message = None  # Initialize the success message variable
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.ticket_maker = user.username  # Assign the logged-in user as the uploader
            ticket.save()
            success_message = 'Ticket sent successfully'  # Set the success message
            return redirect('CreateTicket')
    else:
        form = TicketForm()
    return render(request, 'registration/CreateTicket.html', {'form': form, 'user': user, 'success_message': success_message})

def home(request):
    
    return render(request, 'registration/home.html')


def ticket(request):
    user_id = request.session.get('user_id')
    user = SiteUser.objects.get(id=user_id)
    tickets = Ticket.objects.filter(ticket_maker=user.username)
    print(tickets)
    return render(request, 'registration/ticket.html', {'tickets': tickets, 'user': user})


def ticket_detail(request, ticket_id):
    user_id = request.session.get('user_id')
    user = SiteUser.objects.get(id=user_id)
    ticket = Ticket.objects.get(id=ticket_id)
    
    return render(request, 'registration/ticket_detail.html', {'ticket': ticket, 'user': user})



def user_chat(request):
    user_id = request.session.get('user_id')
    user = SiteUser.objects.get(id=user_id)
    print(request.user.username)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            
            new_message = Message.objects.create(MessageSender=user, Message=message)
            
            return redirect('user_chat')  # Redirect to prevent form resubmission
    else:
        form = MessageForm()
    messages = Message.objects.filter(MessageSender=user)
    return render(request, 'registration/chat.html', {'form': form, 'messages': messages,'user': user})

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            # For example, save it to the database
            feedback_instance = form.save(commit=False)
            feedback_instance.user = request.user  # Assuming you have a user field in your feedback model
            feedback_instance.save()
            return redirect('feedback_success')  # Redirect to a success page
    else:
        form = FeedbackForm()

    return render(request, 'registration/feedback.html', {'form': form})

def feedback_success(request):
    return render(request, 'registration/feedback_success.html')
def package(request):
    return render(request, 'registration/package.html')
def select(request):
    return render(request, 'registration/select.html')
def problem(request):
    return render(request, 'registration/problem.html')
