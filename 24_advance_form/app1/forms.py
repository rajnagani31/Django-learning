from django import forms
from django.core.validators import MinLengthValidator,RegexValidator

# part 1
class demo(forms.Form):
    feild_choice=[
        ('Tech',"Technology"),
        ('art',"Art"),
        ('sports','sports')
    ]

    # basic Field 
    name=forms.CharField()

    email=forms.EmailField()
    pin_code=forms.CharField()

    # Additional Field type 
    age =forms.FloatField()
    date_of_birth=forms.DateField()
    appointment_time=forms.TimeField()
    appointment_date_time=forms.DateTimeField()
    is_subscribed=forms.BooleanField()
    agree_terms=forms.NullBooleanField()

    # choice feild

    gender=forms.ChoiceField(choices=[('F','Femail'),('M','Mail'),('O',"Other")])
    interests_feild=forms.MultipleChoiceField(choices=feild_choice)

    # File and URL Field

    profile_image=forms.ImageField()
    resume = forms.FileField()
    website=forms.URLField()

    # other Specialized Field

    phone_number=forms.RegexField(regex='^\+?1?\d{9,15}$')
    password=forms.CharField(widget=forms.PasswordInput())
    slug=forms.SlugField()
    ip_address=forms.GenericIPAddressField()
    rating=forms.DecimalField()

# data 2
class demo_update(forms.Form):
    name=forms.CharField(
        label="Full name",
        max_length=100,
        label_suffix=":",
        initial="Enter your Full Name",
        help_text="Enter yor right Name",
        validators=[MinLengthValidator(3)]
    )

    email=forms.EmailField(
        label="Email Address",
        disabled=True
    )

    pin_code=forms.IntegerField(
        label="Pin Code",
        min_value=100000,
        max_value=999999,
        error_messages={
            'min_value':'pin code must be least 6 digits.',
            'max_value':'pin code can be at most 6 digits',
        }
    )

    # Additional field

    age=forms.CharField(
        label='Age',
        # min_value=0,

    )

    date_of_birth=forms.DateField(
        label='Data of birth',
        required=False,
        help_text="Enter your Bithe date in YYYY-MM-DD formet"

    )

    appoinment_time=forms.TimeField(
        label="appinment time",
        required=True,
    )

    appoinment_date=forms.DateTimeField(
        label="appoinment date",
        required=True,

    )

    # choice

    gender=forms.ChoiceField(
        label="Gender",
        choices=[('F','Femail'),('M','Mail'),('O',"Other")]
    )

    feild=forms.ChoiceField(
        label="Choice Feild",
        choices=[
        ('Tech',"Technology"),
        ('art',"Art"),
        ('sports','sports')
    ]
    )

    slug=forms.SlugField(
        label="sluge",        
    )


class demo_more_advance(forms.Form):
    name=forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'type here...'}
        )
    )

    password=forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'type here...'}
        )
    )

    key=forms.CharField(
        widget=forms.HiddenInput()
    )

    email=forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder':"Enter a ..@gmail.com"}
        )
    )

    url=forms.URLField(
        widget=forms.URLInput(
            attrs={"type":"text",'placeholder':"https://www.xyz.com"}  
        )
    )

    DOB=forms.CharField(
        widget=forms.TextInput(
            attrs={'type':'date','placeholder':'DD/MM/YYYY'}

        )
    )

    meeting_time=forms.TimeField(
        widget=forms.TimeInput(attrs={'placeholder':'HH-MM-SS','type':'time'})
    )
    date_time=forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type':'datetime-local','placeholder':'DD/MM/YYY HH:MM:SS'})
    )

    # Text area widget

    Discription=forms.CharField(
        widget=forms.Textarea(attrs={'palceholder':'Enter you Discription'})
    )

    boolean=forms.NullBooleanField(
        widget=forms.CheckboxInput()
    )

    null_boolean_field=forms.NullBooleanField(

        widget=forms.NullBooleanSelect()
    )

    choices=forms.ChoiceField(
        choices=[
            ('F','Fmail'),
            ("M","Mail"),
            ('O',"Other")
        ],
        widget=forms.Select()
    )

    multipale_choices=forms.MultipleChoiceField(
        label="Multiple Choice",
        choices=[('tech',"AI Trchnology"),('ml',"ML Technology"),('web3','Blockchain Technology')],
        widget=forms.SelectMultiple()
    )

    redio_choice_field=forms.ChoiceField(
        choices=[('1',"7500 rs."),('2','10,000 rs.')],
        widget=forms.RadioSelect()
    )

    # file uplode

    file_field=forms.FileField(
        label="File Field",
        widget=forms.FileInput()
    )

    image_field=forms.ImageField(
        label='Select image',
        widget=forms.ClearableFileInput
    )

    slug_field=forms.SlugField(
        label="slug",
        widget=forms.TextInput(attrs={'placeholder':'my-slug'})
    )

    ip_address_field=forms.GenericIPAddressField(
        label="IP Address",
        widget=forms.TextInput(attrs={'placeholder':'127.0.0.1'})
    )

    time_duration_field=forms.DurationField(
        label="duration field",
        widget=forms.TextInput({'placeholder':'hh:MM:ss'})
    )

    decimal=forms.DecimalField(
        label="Decimal Field",
        max_digits=5,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'step':'0.1'})
    )

    split_date_time=forms.SplitDateTimeField(
        label="Splite data and time",
        widget=forms.SplitDateTimeWidget(attrs={'type':'datetime-local'})
    )

    split_hidden_date_time=forms.SplitDateTimeField(
        label="Splite Hidden data and time",
        widget=forms.SplitHiddenDateTimeWidget(attrs={'type':'datetime-local'})
    )

