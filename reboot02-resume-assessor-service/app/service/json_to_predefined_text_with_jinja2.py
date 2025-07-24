from jinja2 import Template
class ResumeJsonToText:
    template_str = """
        Name: {{ profile.Name }}
        Skillsets: {{ profile.SkillSets }}
        Work Experience:
        {%- for job in profile.WorkExp %}
        Company: {{ job.Company }} ({{ job.Duration }})
        {%- for proj in job.Project %}
          Role: {{ proj.Role }}
          {%- if proj.Name %}Project: {{ proj.Name }}{% endif %}
          Responsibilities: {{ proj.Responsibilities.replace('\n', ' ') }}
        {%- endfor %}
        {%- endfor %}
      """
    def convert_resume_json_to_text(self, job_application_list):
       template = Template(ResumeJsonToText.template_str)
       domain_specific_resume_list = []
       for resume in job_application_list['Candidate']:
           # domain_specific_resume_list.append(({"resume_id": resume["ApplicationID"], "resume_text": template.render(profile=resume)}))
           resume['resume_text'] = template.render(profile=resume)
       return job_application_list