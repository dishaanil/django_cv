from django.shortcuts import render

def cv_view(request):
    # Education data
    educations = [
        {
            'name': 'Masters in Computer Science',
            'university': 'NYU',
            'start_date': 'Aug 2024',
            'end_date': 'May 2026',
            'marks': '3.8'
        },
        {
            'name': 'Bachelors in Information Science',
            'university': 'PES, Bangalore',
            'start_date': 'July 2017',
            'end_date': 'Aug 2021',
            'marks': '8.9 CGPA'
        }
    ]

    # Experience data
    experiences = [
        {
            'company': 'Wipro',
            'role': 'Software Developer',
            'start_date': 'July 2021',
            'end_date': 'Aug 2024',
            'summary': 'Worked as a full-stack developer for B2C and B2B e-commerce sites'
        },
        {
            'company': 'CustomerInspire',
            'role': 'Intern',
            'start_date': 'Oct 2020',
            'end_date': 'Jan 2021',
            'summary': 'Developed a gamification app for a real-estate company'
        }
    ]

    # Skills data
    skills = ['Java', 'Python']

    # Pass data to template
    context = {
        'educations': educations,
        'experiences': experiences,
        'skills': skills,
    }
    
    return render(request, 'cv/cv.html', context)
