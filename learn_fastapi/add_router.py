from fastapi import APIRouter

router = APIRouter (
    prefix='/add',
    tags=['addition']
)


@router.get('/numbers')
def adding_numbers():
    return {
        'message': 'Using routers for number addition page'
    }



@router.get('/strings')
def adding_strings():
    return {
        'message': 'using routers for string addition page'
    }
