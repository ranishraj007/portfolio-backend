from django.core.management.base import BaseCommand
from django.db import transaction

from portfolio.models import (
    About,
    Education,
    Experience,
    Language,
    Project,
    ProjectDescription,
    Responsibility,
    Skill,
)


PORTFOLIO_DATA = {
    'about': {
        'name': 'Ranish Raj Shrestha',
        'title': 'Computer Engineer (Frontend Developer)',
        'address': 'Chandragiri-09, Kathmandu',
        'contact': '9840800899',
        'email': 'ranish.raj.shrestha@gmail.com',
        'github': 'https://github.com/ranishraj007',
        'linkedin': 'https://www.linkedin.com/in/ranish-raj-shrestha-89aa32207/',
        'summary': (
            'Highly motivated and detail-oriented developer with a solid foundation '
            'in front-end technologies and a growing proficiency in React. Possess '
            'a diverse skill set ranging from traditional programming languages to '
            'modern web development frameworks. Skilled in designing and developing '
            'CSS and SASS components, complemented by practical knowledge in database '
            'tools and queries. Eager to contribute to a dynamic development team and '
            'advance in the field of React development.'
        ),
    },
    'experience': [
        {
            'company': 'Youth Innovation Lab',
            'location': 'Baluwatar, Kathmandu',
            'role': 'Frontend Developer (React)',
            'duration': 'Jul. 2024 - Present',
            'responsibilities': [
                'Developed and deployed multiple web applications using React.',
                'Implemented and tested hooks for client state management.',
                'Integrated RESTful APIs and Axios for data retrieval and editing.',
                'Collaborated with designers and backend teams to ensure seamless development.',
            ],
        },
        {
            'company': 'Entegra Sources Pvt. Ltd',
            'location': 'Baneshwor, Kathmandu',
            'role': 'Electronics Circuit Designer',
            'duration': 'Apr. 2023 - Jun. 2024',
            'responsibilities': [
                'Designed and tested electronic circuits using Proteus and Arduino IDE.',
                'Troubleshoot circuit layouts and documented designs.',
            ],
        },
        {
            'company': 'Mediflow Solution Pvt. Ltd',
            'location': 'Battisputali, Kathmandu',
            'role': 'Web Developer Intern',
            'duration': 'Jul. 2020 - Nov. 2020',
            'responsibilities': [
                'Assisted in developing responsive websites and debugging web applications.',
            ],
        },
    ],
    'education': [
        {
            'institution': 'Acme Engineering College',
            'location': 'Kathmandu',
            'degree': 'Bachelor in Computer Engineering',
            'duration': 'Aug. 2017 - Aug. 2022',
        },
        {
            'institution': 'V.S Niketan College',
            'location': 'Kathmandu',
            'degree': 'HSEB (+2 science)',
            'duration': 'Jun. 2013 - Sep. 2015',
        },
        {
            'institution': 'Pushpasaadan Boarding High School',
            'location': 'Kathmandu',
            'degree': 'SLC',
            'duration': 'Feb. 2007 - Apr. 2013',
        },
    ],
    'projects': [
        {
            'name': 'Bipad Portal',
            'description': [
                'Refactored legacy class-based components into modern functional components using React Hooks.',
                'Optimized data-heavy dashboards and improved rendering performance for large datasets.',
                'Implemented geospatial data visualizations and enhanced UI for disaster monitoring systems.',
                'Focused on performance, scalability, and maintainability for a national-level platform.',
            ],
            'url': 'https://bipadportal.gov.np/',
        },
        {
            'name': 'National Platform for Disaster Risk Reduction (NPDRR)',
            'description': [
                'Built reusable React components using Tailwind CSS and Redux Toolkit.',
                'Integrated APIs for dynamic content and developed fully responsive pages.',
                'Ensured modular code structure, accessibility, and consistency across the platform.',
                'Collaborated with team members to maintain design and development standards.',
            ],
            'url': 'https://npdrr.bipad.gov.np/',
        },
        {
            'name': 'NDRRMA (National Disaster Risk Reduction & Management Authority)',
            'description': [
                'Maintained and improved an existing React-based application for stability and performance.',
                'Debugged critical issues and enhanced UI consistency across modules.',
                'Implemented new features to improve usability and system functionality.',
                'Ensured cross-device compatibility and compliance with government standards.',
            ],
            'url': 'https://ndrrma.gov.np/np',
        },
        {
            'name': 'HEAT AI',
            'description': [
                'Developed multilingual and responsive interfaces using React, Tailwind CSS, and Redux Toolkit.',
                'Integrated Mapbox for geospatial visualization and built custom hooks for dynamic rendering.',
                'Handled API integration for dynamic data and real-time updates.',
                'Focused on performance optimization and clean, scalable component architecture.',
            ],
            'url': 'https://heatai.org/',
        },
        {
            'name': 'United States Youth Council (USYC)',
            'description': [
                'Developed a responsive and mobile-friendly website using React and Tailwind CSS.',
                'Built reusable UI components with a focus on clean and maintainable design.',
                'Optimized performance for faster load times and smoother user experience.',
                'Ensured cross-browser compatibility and accessibility.',
            ],
            'url': 'https://www.usycn.org/',
        },
        {
            'name': 'Creators Mela',
            'description': [
                'Built responsive and visually engaging event pages using React and Tailwind CSS.',
                'Improved performance and optimized assets for faster loading.',
                'Enhanced navigation and user experience across devices.',
                'Maintained consistent UI design aligned with event branding.',
            ],
            'url': 'https://usembassynepal.events/',
        },
        {
            'name': 'Tag Me',
            'description': [
                'Developed interactive UI modules and handled complex form-based data collection.',
                'Built reusable components using React and Tailwind CSS for consistent UI.',
                'Integrated APIs for crowdsourced data submission and management.',
                'Focused on usability, validation, and smooth user interaction.',
            ],
            'url': 'https://tagme.yilab.org.np/',
        },
        {
            'name': 'Youth Innovation Lab (Yi Lab)',
            'description': [
                'Established frontend architecture and coding best practices for multiple projects.',
                "Built and maintained the organization's main website using React.",
                'Improved performance, SEO, and accessibility for global users.',
                'Collaborated with cross-functional teams to ensure scalability and consistency.',
            ],
            'url': 'https://youthinnovationlab.org/',
        },
        {
            'name': 'Shikshya',
            'description': [
                'Contributed to frontend development using React with a focus on debugging and testing.',
                'Fixed UI bugs and improved overall platform stability.',
                'Enhanced user experience through small but impactful UI improvements.',
                'Worked closely with the team to ensure consistent behavior across features.',
            ],
            'url': 'https://shikshya.org/',
        },
        {
            'name': 'Risk AI',
            'description': [
                'Developed frontend interfaces for an AI-based risk analysis platform.',
                'Integrated APIs to enable real-time chat functionality for disaster risk insights.',
                'Implemented responsive UI and modern styling using React and Tailwind CSS.',
                'Focused on performance, usability, and clean component structure.',
            ],
            'url': 'https://riskgent.com/',
        },
    ],
    'skills': [
        'HTML',
        'CSS',
        'JavaScript (ES6+)',
        'Python (Basic)',
        'C++ (Basic)',
        'React.js',
        'Next.js',
        'Redux',
        'remix.js',
        'three.js',
        'Redux Toolkit',
        'React Query (TanStack Query)',
        'Axios',
        'Bootstrap',
        'Tailwind CSS',
        'Material UI (MUI)',
        'Django REST Framework',
        'REST API Integration',
        'Git',
        'GitHub',
        'Postman',
        'Docker (Basic)',
        'ESLint',
        'Prettier',
        'Husky',
        'lint-staged',
        'Mapbox GL JS',
        'Mapbox Studio',
        'Linux (CLI, basic system operations)',
        'Windows',
        'Problem Solving',
        'Critical Thinking',
        'Communication',
        'Time Management',
        'Analytical Thinking',
        'Observation',
    ],
    'languages': ['Nepali', 'English', 'Newari', 'Hindi'],
}


class Command(BaseCommand):
    help = 'Load the current frontend portfolioData.ts content into the database.'

    @transaction.atomic
    def handle(self, *args, **options):
        About.objects.all().delete()
        Experience.objects.all().delete()
        Education.objects.all().delete()
        Project.objects.all().delete()
        Skill.objects.all().delete()
        Language.objects.all().delete()

        About.objects.create(**PORTFOLIO_DATA['about'])

        for order, item in enumerate(PORTFOLIO_DATA['experience']):
            experience_data = item.copy()
            responsibilities = experience_data.pop('responsibilities')
            experience = Experience.objects.create(order=order, **experience_data)
            Responsibility.objects.bulk_create(
                [
                    Responsibility(experience=experience, text=text, order=index)
                    for index, text in enumerate(responsibilities)
                ]
            )

        Education.objects.bulk_create(
            [
                Education(order=order, **item)
                for order, item in enumerate(PORTFOLIO_DATA['education'])
            ]
        )

        for order, item in enumerate(PORTFOLIO_DATA['projects']):
            project_data = item.copy()
            descriptions = project_data.pop('description')
            project = Project.objects.create(order=order, **project_data)
            ProjectDescription.objects.bulk_create(
                [
                    ProjectDescription(project=project, text=text, order=index)
                    for index, text in enumerate(descriptions)
                ]
            )

        Skill.objects.bulk_create(
            [
                Skill(name=name, order=order)
                for order, name in enumerate(PORTFOLIO_DATA['skills'])
            ]
        )
        Language.objects.bulk_create(
            [
                Language(name=name, order=order)
                for order, name in enumerate(PORTFOLIO_DATA['languages'])
            ]
        )

        self.stdout.write(self.style.SUCCESS('Portfolio data seeded successfully.'))
