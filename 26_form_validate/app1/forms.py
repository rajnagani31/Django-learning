from django import forms 

class login(forms.Form):
    name=forms.CharField()
    city=forms.CharField()


# clean and validate feild specific
    # def clean_name(self):
    #     name_value=self.cleaned_data['name']
    #     if len(name_value) < 4:
    #             raise forms.ValidationError('Enter more then or equal 4 char')

    #     return name_value 
    
    # def clean_city(self):
    #     city_value=self.cleaned_data['city']
    #     if len(city_value) < 5:
    #         raise forms.ValidationError('enter a more then or equal 5 char')
            
    #     return city_value
    
# clean and validate feild Django form at all in one    


    def clean(self):
        cleaned_data=super().clean()

        name_value=cleaned_data.get('name')
        city_value=cleaned_data.get('city')

        if name_value and len(name_value) < 4:
             self.add_error('name',"Enter a more than or equal to 4")
        if 'r' not in name_value:
            self.add_error('name','include "r" char')     

        if city_value and len(city_value) <5:
             self.add_error('city',"Enter a more than or equal to 5")     
