from datetime import datetime
from api_eng_.models import FormulaHistory
from api_eng_.operators import RegisteredOperatorsEngine, mathmatic_operators
from authapp.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from api_eng_ import common

from api_eng_ import local_settings


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    """
    General function designed to return sarver status OK
    for logged-on users only
    """
    context = {
        'status': status.HTTP_200_OK,
        'result': common.SERVER_ON,
        'date': datetime.now().strftime('%d/%m/%y %H:%M:%S'),
    }
    return Response(data=context, status=status.HTTP_200_OK)


def validate_empty_plus(validate_string):
    """
    Param : validate_string (formula)
    Type : string
    Return : insert a plus sign if necessary
    """
    if ' ' in validate_string:
        str_no_spaces = validate_string.replace(' ', '')
        if str_no_spaces is '':
            return "+"
    return (validate_string)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_list(request):
    result = common.EMPTY_OP_LIST
    context = {
        'time': 0,
        'status': status.HTTP_200_OK,
        'result': result,
    }
    operators = local_settings.regi
    result = operators.get_list()
    context['result'] = result
    return Response(data=context, status=context['status'])
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def eval_any_dev(request):
    """
    Generic function that handles numbers and operators 
    allowed at REST API (for DEV no db store)
    """
    return eval_any(request=request, data_store=False)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def eval_any(request, data_store=False):
    """
    Generic function that handles numbers and operators 
    allowed at REST API 

    key:formula
    INFO: <FV:float_value><MO:mathematic_operator>
    structure: <FV><MO><FV> / <MO><FV> / <FV><MO>
    """

    def store_history(results, is_done):
        user_obj = User.objects.get(id=request.user.id)
        if not User:
            raise User.DoesNotExist
        formula_history_obj = FormulaHistory.objects.create(
            user=user_obj,
            val1=val1,
            val2=val2,
            operator=mathematica_operator,
            result=results,
            is_done=is_done,
        )
        formula_history_obj.save()

    scope_timer = common.local_timer()
    result = common.UNDEFINED_FORMULA
    operators = local_settings.regi
    val1 = val2 = mathematica_operator = ''
    context = {
        'time': 0,
        'status': status.HTTP_200_OK,
        'result': result,
    }
    try:
        if request.method == 'GET':
            val1 = request.GET["val1"]
            val2 = request.GET["val2"]
            mathematica_operator = request.GET["mathematica_operator"]
            mathematica_operator = validate_empty_plus(mathematica_operator)
        elif request.method == 'POST':
            val1 = request.POST.get("val1", None)
            val2 = request.POST.get("val2", None)
            mathematica_operator = request.POST.get("mathematica_operator", None)
        else:
            context['status'] = status.BAD_REQ_ERROR
            context['result'] = '{}'.format(common.GENERAL_ERROR)
            return Response(data=context, status=status.HTTP_400_BAD_REQUEST)
        result = operators.eval(op=mathematica_operator, n=val1, m=val2)
        context['time'] = scope_timer.get_current_time()
        context['result'] = result if result or result == 0.0 else common.UNDEFINED_FORMULA
        if data_store:
            store_history(result=result, is_done=True)
        return Response(data=context, status=status.HTTP_200_OK)
    except SyntaxError as sxr:
        context['result'] = '{}'.format(common.SYNTAX_ERROR)
        pass
    except TypeError as txr:
        context['result'] = '{}'.format(common.TYPE_ERROR)
        pass
    except KeyError as kxr:
        context['result'] = '{}'.format(common.KEY_ERROR)
        pass
    except Exception as exr:
        context['result'] = '{}'.format(common.GENERAL_ERROR)
        pass
    context['time'] = scope_timer.get_current_time()
    context['status'] = status.HTTP_201_CREATED
    if data_store:  # bad data is_done=False
        store_history(result=result, is_done=False)
    return Response(data=context, status=context['status'])
