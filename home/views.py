from django.shortcuts import render


def main(request):
    # HEADER_NAME = 'head'
    # ABOUT_NAME = 'about us'
    # SPACER_NAME = 'spacer'
    #
    # header = Header.objects.get(title=HEADER_NAME)
    # about = About.objects.get(title=ABOUT_NAME)
    # services = Services.objects.all()
    # spacer = Spacer.objects.get(title=SPACER_NAME)
    # works = Work.objects.all()
    # team = Developer.objects.all()

    return render(request, 'home/index.html', locals())
