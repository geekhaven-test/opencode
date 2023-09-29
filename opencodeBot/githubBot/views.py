import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

def commentOnAPullRequest(repo, PRNumber, comment):
    requests.post(
        "https://api.github.com/repos/opencodeiiita/"
        + repo
        + "/issues/"
        + str(PRNumber)
        + "/comments",
        json={"body": comment},
        # headers={"Authorization": "token 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"},
    )

@api_view(['POST'])
def issueComment(request):
    if request.data and 'action' in request.data  and request.data.action == 'created':
        # if "sender" in request.data and "login" in request.data.sender:


        print(request)
    return Response(status=202)
