from django.template import RequestContext
from django.shortcuts import render_to_response

class OutOfRangeError(ValueError): pass
class NotIntegerError(ValueError): pass

# ...
def create(request):
    """
    Create a new project. The view is build in HTML5 doctype.
    Project required: Project name, project owner and description
    """ 
    
    p = 3
    return render_to_response('projects/create.html', {'poll': p},
                               context_instance=RequestContext(request))
    
    
def statistics(request, project_id):
    """
    Statistics of selected project.
    
    Required parameters: project_id
    
    After request:
    Connect to API and get cached statistics results
    
    Features:
    - Cached: Results are cached for 2,5 hours
    - Cronjob: Create new results every 2,5 hours
    """
    
    p = 3
    return render_to_response('projects/statistics.html', {'poll': p},
                               context_instance=RequestContext(request))

def remove(request, project_id):
    """
    Page to confirm the remove action
    
    Required parameters:
    - @project_id
    """
    
    if not project_id:
        raise NotIntegerError('No project id found')
    
    
    p = 3
    return render_to_response('projects/remove.html', {'poll': p},
                               context_instance=RequestContext(request))
    
    
def build(request):
    """
    Show information about selected build
    
    Required parameters:
    - project_id
    - version
    """
    
    p = 3
    return render_to_response('projects/build.html', {'poll': p},
                               context_instance=RequestContext(request))

    
def builds_overview(request):
    
    p = 3
    return render_to_response('projects/build/overview.html', {'poll': p},
                               context_instance=RequestContext(request))

