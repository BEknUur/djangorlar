#django modules
from django.core.management import BaseCommand
from django.db.models import Q, Count, Avg, Min, Sum, Case, When, Value, CharField, F, ExpressionWrapper, fields, Max
from django.db.models.functions import Concat, ExtractYear, Now
from django.utils import timezone
#python modules
from datetime import timedelta, date
#project modules
from apps.users.models import CustomUser


class Command(BaseCommand):
    """50 ORM queries for practice"""

    def handle(self, *args, **options):
        q1 = CustomUser.objects.filter(is_active=True)
        self.stdout.write(f"2.1 - Active users: {q1.count()}")

        q2 = CustomUser.objects.filter(email__endswith='@gmail.com')
        self.stdout.write(f"2.2 - Gmail users: {q2.count()}")

        q3 = CustomUser.objects.filter(city='Almaty')
        self.stdout.write(f"2.3 - Almaty users: {q3.count()}")

        q4 = CustomUser.objects.exclude(city='Almaty')
        self.stdout.write(f"2.4 - Not Almaty users: {q4.count()}")

        q5 = CustomUser.objects.filter(salary__gt=500000)
        self.stdout.write(f"2.5 - Users with salary > 500000: {q5.count()}")

        q6 = CustomUser.objects.filter(department='IT', country='Kazakhstan')
        self.stdout.write(f"2.6 - IT users from Kazakhstan: {q6.count()}")

        q7 = CustomUser.objects.filter(birth_date__isnull=True)
        self.stdout.write(f"2.7 - Users without birth_date: {q7.count()}")

        q8 = CustomUser.objects.filter(first_name__istartswith='A')
        self.stdout.write(f"2.8 - Users with first_name starting with A: {q8.count()}")

        q9 = CustomUser.objects.count()
        self.stdout.write(f"2.9 - Total users: {q9}")

        q10 = CustomUser.objects.order_by('-date_joined')[:20]
        self.stdout.write(f"2.10 - First 20 users by date_joined: {q10.count()}")

        q11 = CustomUser.objects.values_list('city', flat=True).distinct()
        self.stdout.write(f"2.11 - Distinct cities: {q11.count()}")

        q12 = CustomUser.objects.filter(department='Sales').count()
        self.stdout.write(f"2.12 - Sales department users: {q12}")

        seven_days_ago = timezone.now() - timedelta(days=7)
        q13 = CustomUser.objects.filter(last_login__gte=seven_days_ago).count()
        self.stdout.write(f"2.13 - Users logged in last 7 days: {q13}")

        q14 = CustomUser.objects.filter(Q(first_name__icontains='bek') | Q(last_name__icontains='bek'))
        self.stdout.write(f"2.14 - Users with 'bek' in name: {q14.count()}")

        q15 = CustomUser.objects.filter(salary__gte=300000, salary__lte=700000)
        self.stdout.write(f"2.15 - Users with salary 300k-700k: {q15.count()}")

        q16 = CustomUser.objects.filter(department__in=['IT', 'HR', 'Finance'])
        self.stdout.write(f"2.16 - Users in IT/HR/Finance: {q16.count()}")

        q17 = CustomUser.objects.values('department').annotate(count=Count('id'))
        self.stdout.write(f"2.17 - Users per department: {q17.count()} departments")

        q18 = CustomUser.objects.values('department').annotate(count=Count('id')).order_by('-count')
        self.stdout.write(f"2.18 - Departments by user count (desc): {list(q18)}")

        q19 = CustomUser.objects.values('city').annotate(count=Count('id')).order_by('-count')[:5]
        self.stdout.write(f"2.19 - Top 5 cities: {list(q19)}")

        q20 = CustomUser.objects.filter(last_login__isnull=True)
        self.stdout.write(f"2.20 - Users never logged in: {q20.count()}")

        q21 = CustomUser.objects.aggregate(avg_salary=Avg('salary'))
        self.stdout.write(f"2.21 - Average salary: {q21['avg_salary']}")

        q22 = CustomUser.objects.aggregate(min_salary=Min('salary'), max_salary=Max('salary'))
        self.stdout.write(f"2.22 - Min/Max salary: {q22}")

        q23 = CustomUser.objects.filter(phone__contains='+7')
        self.stdout.write(f"2.23 - Users with +7 phone: {q23.count()}")

        q24 = CustomUser.objects.annotate(full_name=Concat('first_name', Value(' '), 'last_name'))
        self.stdout.write(f"2.24 - Users with full_name: {q24.count()}")

        q25 = CustomUser.objects.filter(birth_date__isnull=False).annotate(
            birth_year=ExtractYear('birth_date')
        ).order_by('birth_year')
        self.stdout.write(f"2.25 - Users with birth_year: {q25.count()}")

        q26 = CustomUser.objects.filter(birth_date__month=5)
        self.stdout.write(f"2.26 - Users born in May: {q26.count()}")

        q27 = CustomUser.objects.filter(role='manager', salary__gt=400000)
        self.stdout.write(f"2.27 - Managers with salary > 400k: {q27.count()}")

        q28 = CustomUser.objects.filter(Q(role='employee') | Q(department='HR'))
        self.stdout.write(f"2.28 - Employees or HR: {q28.count()}")

        q29 = CustomUser.objects.filter(is_active=True).values('city').annotate(count=Count('id'))
        self.stdout.write(f"2.29 - Active users per city: {q29.count()} cities")

        q30 = CustomUser.objects.order_by('date_joined')[:10]
        self.stdout.write(f"2.30 - 10 earliest users: {q30.count()}")

        q31 = CustomUser.objects.filter(city__istartswith='A', salary__gt=300000)
        self.stdout.write(f"2.31 - Users from A-cities with salary > 300k: {q31.count()}")

        q32 = CustomUser.objects.filter(Q(department__isnull=True) | Q(department=''))
        self.stdout.write(f"2.32 - Users without department: {q32.count()}")

        q33 = CustomUser.objects.values('country').annotate(
            count=Count('id'),
            avg_salary=Avg('salary')
        )
        self.stdout.write(f"2.33 - Stats by country: {q33.count()} countries")

        q34 = CustomUser.objects.filter(is_staff=True).order_by('-last_login')
        self.stdout.write(f"2.34 - Staff users: {q34.count()}")

        q35 = CustomUser.objects.exclude(email__contains='example.com')
        self.stdout.write(f"2.35 - Users without example.com: {q35.count()}")

        avg_salary = CustomUser.objects.aggregate(Avg('salary'))['salary__avg']
        q36 = CustomUser.objects.filter(salary__gt=avg_salary)
        self.stdout.write(f"2.36 - Users above avg salary: {q36.count()}")

        q37 = CustomUser.objects.values('email').annotate(count=Count('id')).filter(count__gt=1)
        self.stdout.write(f"2.37 - Duplicate emails: {q37.count()}")

        q38 = CustomUser.objects.annotate(
            salary_level=Case(
                When(salary__lt=300000, then=Value('low')),
                When(salary__gte=300000, salary__lte=700000, then=Value('medium')),
                When(salary__gt=700000, then=Value('high')),
                default=Value('unknown'),
                output_field=CharField()
            )
        ).order_by('salary_level')
        self.stdout.write(f"2.38 - Users with salary_level: {q38.count()}")

        current_year = timezone.now().year
        q39 = CustomUser.objects.filter(date_joined__year=current_year)
        self.stdout.write(f"2.39 - Users joined this year: {q39.count()}")

        q40 = CustomUser.objects.values('department').annotate(total_salary=Sum('salary'))
        self.stdout.write(f"2.40 - Payroll by department: {list(q40)}")

        q41 = CustomUser.objects.filter(department='IT', last_login__isnull=True)
        self.stdout.write(f"2.41 - IT users never logged in: {q41.count()}")

        q42 = CustomUser.objects.filter(
            country='Kazakhstan'
        ).filter(Q(city__isnull=True) | Q(city=''))
        self.stdout.write(f"2.42 - Kazakhstan users without city: {q42.count()}")

        q43 = CustomUser.objects.filter(birth_date__lt=date(1990, 1, 1), salary__isnull=False)
        self.stdout.write(f"2.43 - Users born before 1990 with salary: {q43.count()}")

        q44 = CustomUser.objects.annotate(
            days_since_joined=ExpressionWrapper(
                Now() - F('date_joined'),
                output_field=fields.DurationField()
            )
        )
        self.stdout.write(f"2.44 - Users with days_since_joined: {q44.count()}")

        q45 = CustomUser.objects.filter(
            department='Sales',
            email__endswith='@gmail.com',
            salary__gt=350000
        )
        self.stdout.write(f"2.45 - Sales Gmail users with salary > 350k: {q45.count()}")

        q46 = CustomUser.objects.order_by('country', '-salary')
        self.stdout.write(f"2.46 - Users ordered by country, -salary: {q46.count()}")

        q47 = CustomUser.objects.values('role').annotate(count=Count('id')).filter(count__gt=100)
        self.stdout.write(f"2.47 - Roles with > 100 users: {list(q47)}")

        q48 = CustomUser.objects.filter(last_login__lt=F('date_joined'))
        self.stdout.write(f"2.48 - Inconsistent login dates: {q48.count()}")

        q49 = CustomUser.objects.annotate(
            is_senior=Case(
                When(birth_date__lt=date(1985, 1, 1), then=Value(True)),
                default=Value(False),
                output_field=fields.BooleanField()
            )
        )
        self.stdout.write(f"2.49 - Users with is_senior: {q49.count()}")

        q50 = CustomUser.objects.values('department').annotate(
            avg_salary=Avg('salary'),
            user_count=Count('id')
        ).filter(user_count__gte=20).order_by('-avg_salary')
        self.stdout.write(f"2.50 - Departments (20+ users) by avg salary: {list(q50)}")

        self.stdout.write(self.style.SUCCESS('✓ All 50 queries executed successfully!'))

      
