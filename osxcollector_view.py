def replace_underscore(value):
    return value.replace('_', ' ')

def get_ctx_result(result):

    ctx_result = {}

    ctx_result['summary'] = result.get_summary()
    ctx_result['param'] = result.get_param()
    ctx_result['status'] = result.get_status()

    if (not ctx_result['status']):
        ctx_result['message'] = result.get_message()

    data = result.get_data()

    if (not data):
        return ctx_result

    data = data[0]

    ctx_result['data'] = data

    return ctx_result


def get_system_info(provides, all_app_runs, context):

    context['results'] = results = []
    for summary, action_results in all_app_runs:
        for result in action_results:

            ctx_result = get_ctx_result(result)
            if (not ctx_result):
                continue
            results.append(ctx_result)
    # print context
    return 'osxc_display_info.html'
