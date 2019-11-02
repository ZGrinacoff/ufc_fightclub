from wtforms import Form, StringField, TextAreaField, validators


class SubmissionForm(Form):
    blue_height = StringField('B_Height_cms', [validators.Length(min=1, max=300)])
    blue_reach = StringField('B_Reach_cms', [validators.Length(min=1, max=300)])
    blue_weight = StringField('B_Weight_lbs', [validators.Length(min=1, max=300)])
    red_height = StringField('R_Height_cms', [validators.Length(min=1, max=300)])
    red_reach = StringField('R_Reach_cms', [validators.Length(min=1, max=300)])
    red_weight = StringField('R_Weight_lbs', [validators.Length(min=1, max=300)])
    blue_age = StringField('B_age', [validators.Length(min=1, max=300)])
    red_age = StringField('R_age', [validators.Length(min=1, max=300)])
    blue_text = TextAreaField('Text', [validators.Length(min=1, max=500)])
    red_text = TextAreaField('Text', [validators.Length(min=1, max=500)])