import csv
import random
from faker import Faker
import pandas as pd

from datetime import datetime

fake = Faker()


# Tech company job description
job_description_react_one = """Job Description Summary

Experience : 5 - 10 years

We are looking for a passionate and experienced Frontend Developer with strong expertise in React.js, JavaScript, and TypeScript to join our high-performing engineering team. The ideal candidate should also be comfortable working with Angular and have working knowledge of Node.js for frontend tooling and integration. You will be responsible for building responsive, scalable, and maintainable web applications that deliver an excellent user experience. The role involves close collaboration with product, design, and backend engineering teams in an agile environment.

Job Description

Required Skills:

Strong proficiency in React.js and modern JavaScript (ES6+), including functional components and hooks.
Experience with TypeScript for scalable and type-safe frontend development.
Hands-on experience with HTML5, CSS3, and frontend frameworks like Bootstrap or Material UI.
Proficiency in Angular (any recent version) for maintaining or migrating legacy modules.
Familiarity with frontend build tools and environments (Webpack, Vite, Babel, npm/yarn).
Basic understanding of Node.js and Express for frontend middleware and integration.
Experience in consuming RESTful APIs and handling async data flows (fetch, axios).
Solid grasp of UI/UX best practices, accessibility (WCAG), and responsive web design.
Ability to translate Figma/Sketch designs into interactive, production-ready UI components.
Experience working in Agile/Scrum teams and using version control tools like Git.
"""

engineer_title = ["Senior Software Engineer", "Software Engineer", "Software Developer", "Tech Lead", "Technical Lead", "Engineering Lead", "Software Development Engineer", "SSE", "SDE", "SE"]
tech_core_skills_React = ["React", "HTML/CSS", "Bootstrap", "UX", "Javascript", "Accessibility", "Angular", "ReactJs", "VueJs",
                          "Figma", "Typescript", "Material UI", "Redux", "CSS", "ES6", "React.js", "CSS3", "Node.js", "NodeJs", "Express",
                          "ExpressJs", "Express.js", "WCAG", "UI/UX", "Frontend", "UI", "Wiremocks"]
tech_core_skills_others = ["Java", "Python", "Selenium", "Spring Boot", "CI/CD", ".NET", "Kubernetes", "Scala", "Hibernate", "AWS", "GCP", "Apache Spark", "Azure", "SQL", "Docker", "Jenkins", "Git",
                    "Microservices", "REST APIs"]

def create_resume_react_set_one(n):
    name = fake.name()
    company = fake.company()
    project = fake.bs().title()
    role = fake.job()


    positive_resp_list = [ """Developed and maintained React.js SPAs using functional components and hooks.
Used TypeScript and ESLint for scalable and maintainable code quality.
Collaborated with designers to implement pixel-perfect UI with HTML5, CSS3, and Bootstrap.
Integrated frontend with REST APIs and managed data flow using Axios.
Worked on modularizing legacy Angular components as part of migration roadmap.""",
    """Created responsive UIs using React, Bootstrap, and Material UI in a product-based SaaS environment.
Implemented form validation and user flows using React Hook Form and TypeScript.
Connected frontend with Node.js backend via RESTful APIs.
Participated in daily stand-ups and delivered features using Agile methodology.
Performed cross-browser testing and WCAG accessibility compliance.""",
    """Worked on an enterprise portal using Angular 11 and migrated parts to React.js.
Developed reusable UI components in TypeScript and styled them using SCSS and Bootstrap.
Configured Webpack and Babel for custom frontend builds.
Consumed REST endpoints and managed state locally using React Context.
Collaborated with backend team using Git, Jira, and Figma.""",
    """Built and maintained a B2B dashboard using React and TypeScript.
Used HTML5 semantics and CSS Flex/Grid for responsive layout.
Integrated UI with Node.js-based authentication and analytics endpoints.
Contributed to Angular module refactoring during tech debt cleanup.
Wrote component-level tests using React Testing Library and Jest.""",
    """Developed a customer onboarding wizard in React using TypeScript and Formik.
Styled complex layouts using Bootstrap 5 and custom CSS3.
Set up frontend proxy and middleware using Express and Node.js.
Worked with REST APIs and handled global errors and retries.
Participated in weekly grooming, sprint demos, and retrospectives.""",
    """Led UI revamp using React with functional components, JSX, and useEffect hooks.
Ported components from Angular to React while ensuring design consistency.
Used TypeScript to enforce prop types and catch runtime issues early.
Implemented lazy loading and performance optimizations with Webpack.
Handled responsive breakpoints using Bootstrap utility classes.""",
    """Worked on multilingual support in React using i18next and dynamic content binding.
Maintained legacy Angular components for admin panel use-cases.
Used CSS3 animations and transitions to enhance UI responsiveness.
Managed package dependencies via npm and code-split routes with React Router.
Integrated UI layer with a Node.js proxy layer to simulate backend.""",
    """Built internal tools in React with Redux and TypeScript for data visualization.
Styled components using Bootstrap and custom SCSS themes.
Implemented role-based access with Node.js middleware for the frontend routes.
Fetched paginated data from REST APIs and handled caching.
Worked with designers to implement accessibility and contrast fixes.""",
    """Created modular React component libraries in TypeScript and documented with Storybook.
Participated in migration of AngularJS legacy features to React.
Used Fetch and Axios for REST API integration and state management via hooks.
Implemented form validation, dropdown filters, and responsive tables using Bootstrap.
Collaborated with backend team on contract-first API design.""",
    """Developed analytics dashboards using React.js, React Router, and TypeScript.
Set up Jest and React Testing Library for unit and integration testing.
Used Bootstrap for layout grid system and responsive navigation.
Connected with Express.js middle layer for secure API routing.
Contributed to frontend architecture discussions and PR reviews.""",
    """Worked on a multi-tenant SaaS admin panel in React with full TypeScript coverage.
Styled components using Bootstrap grid system and custom utilities.
Handled auth integration with Node.js backend using JWT tokens.
Refactored older Angular services and ported logic into React components.
Configured ESLint, Prettier, and Git hooks for code quality enforcement.""",
    """Built React-based dashboards for operations monitoring with Axios and fetch.
Managed data-driven UI rendering based on RESTful API states.
Used Bootstrap modals, tooltips, and cards for UI consistency.
Developed CLI tooling using Node.js to scaffold React components.
Wrote unit tests for critical user journeys using Jest.""",
    """Migrated UI code from Angular to React.js for an internal CRM.
Built shared UI library using React, Bootstrap, and SCSS variables.
Used TypeScript for props typing and form schema validation.
Integrated frontend with Node.js middleware handling SSO tokens.
Followed WCAG guidelines for accessibility and keyboard navigation.""",
    """Developed frontend tools for an e-learning platform in React and TypeScript.
Used Bootstrap, Flexbox, and CSS Grid for fully responsive layouts.
Configured API interceptors and token refresh logic with Axios.
Implemented toast messages, loaders, and route guards using hooks.
Worked in a Git-based Agile team using GitHub Actions and Jira.""",
    """Built React SPAs integrated with backend microservices via REST APIs.
Used modern JavaScript (ES6+), TypeScript, and Bootstrap 4/5.
Styled and refactored AngularJS legacy code during phased migration.
Set up middleware proxy in Node.js to bypass CORS in development.
Worked on cross-browser compatibility and layout consistency across viewports."""
                           ]

    negative_resp_list = [ """Worked extensively on backend systems using Java and Spring Boot.
Built REST APIs and integrated Kafka for messaging.
No experience with frontend frameworks like React or Angular.""",
    """Developed microservices in Go and deployed on Kubernetes.
Focused entirely on backend architecture and database design.
No frontend technologies used in role.""",
    """Built machine learning pipelines in Python and deployed models with Flask APIs.
Worked exclusively on model training and inference logic.
Frontend tasks were handled by a separate UI team.""",
    """Led data engineering projects using Apache Spark and Scala.
Built ETL workflows and batch pipelines for data warehousing.
Did not contribute to any UI or frontend development.""",
    """Built automation tools using Java and Selenium for QA teams.
Created test scripts and integrated CI pipelines.
No involvement in web app development or frontend design.""",
    """Developed RESTful services for e-commerce APIs using .NET Core.
Managed entity framework-based persistence and middleware.
No React, Angular, or frontend skills applied.""",
    """Worked on cloud infrastructure automation using Terraform and Ansible.
Configured cloud networking and monitoring dashboards.
Role was DevOps-focused, not full-stack or UI-related.""",
    """Built backend APIs in Node.js and Express with MongoDB.
Did not contribute to frontend implementation.
No use of React, Bootstrap, or UI frameworks.""",
    """Contributed to backend analytics systems using Rust and PostgreSQL.
Wrote backend schedulers and batch data aggregators.
Frontend and UI were out of scope for the project.""",
                           """Developed native Android apps using Kotlin for a ride-sharing platform.
                          Worked on UI animations and background sync in mobile apps.
                          No web technologies or frontend libraries used.""",
                           """Built iOS applications using Swift and SwiftUI for healthcare tracking.
                       Implemented local persistence and biometric login.
                       No experience in JavaScript, React, or HTML.""",
                           """Worked as a WordPress developer customizing plugins and themes.
                       Used PHP and jQuery for minor frontend tweaks.
                       No experience with React, Angular, or TypeScript.""",
                           """Built desktop applications using Electron and Python.
                       Handled inter-process communication and native OS integration.
                       No exposure to modern frontend web stacks.""",
                           """Developed Unity-based educational games using C#.
                       Handled physics, rendering, and in-game animations.
                       Not involved in frontend web development.""",
                           """Worked on mainframe systems using COBOL and JCL for a financial institution.
                       Focused on legacy batch processing and terminal interfaces.
                       No frontend experience, not aligned with modern web stack."""
                           ]

    positive_skills = tech_core_skills_React
    negative_skills = tech_core_skills_others

    result = []
    for _ in range(n):
            start1= fake.date_between(start_date='-8y', end_date='-2y')
            end1 = fake.date_between(start_date=start1, end_date='today')
            duration1 = f"{start1.strftime('%b %Y')} – {end1.strftime('%b %Y')}"
            responsibilities = random.choice(positive_resp_list)
            ranges = [(4,13)]
            selected_range = random.choice(ranges)
            exp = random.randint(selected_range[0], selected_range[1])
            resume_positive = (f"Name: {fake.name()}\n"
            f"Skillsets: {', '.join(random.sample(positive_skills, k=min(6, len(positive_skills))))}\n"
            f"Years of Experience: {exp}\n"
            f"Work Experience:\n"
            f"Company: {fake.company()}\n"
            f"Duration: {duration1}\n"
            f"Project: {fake.bs().title()}\n"
            f"Role: {random.choice(engineer_title)}\n"
            f"Responsibilities: {responsibilities}\n")

            start2 = fake.date_between(start_date='-8y', end_date='-2y')
            end2 = fake.date_between(start_date=start2, end_date='today')
            duration2 = f"{start2.strftime('%b %Y')} – {end2.strftime('%b %Y')}"
            responsibilities = random.choice(negative_resp_list)
            exp = random.randint(5, 13)
            resume_negative = (f"Name: {fake.name()}\n"
            f"Skillsets: {', '.join(random.sample(negative_skills, k=min(6, len(negative_skills))))}\n"
            f"Years of Experience: {exp}\n"
            f"Work Experience:\n"
            f"Company: {fake.company()}\n"
            f"Duration: {duration2}\n"
            f"Project: {fake.bs().title()}\n"
            f"Role: {random.choice(engineer_title)}\n"
            f"Responsibilities: {responsibilities}\n")

            result.append((job_description_react_one, resume_positive, resume_negative))
    print(result)
    return result