import groupdocs_conversion_cloud

app_sid = '49a8e88d-8d58-40ce-9aa6-d7e9e995c9c6'
app_key = 'f7d7c610bc7776b526aee23866cb3bb2'

convert_api = groupdocs_conversion_cloud.ConvertApi.from_keys(app_sid, app_key)
file_api = groupdocs_conversion_cloud.FileApi.from_keys(app_sid, app_key)

try:
    file_name = 'course.pdf'
    remote_name = 'course.pdf'
    output_name = 'course.docx'
    strformat = 'docx'

    request_upload = groupdocs_conversion_cloud.UploadFileRequest(remote_name, file_name)
    respond_upload = file_api.upload_file(request_upload)
    settings = groupdocs_conversion_cloud.ConvertSettings()
    settings.file_path = remote_name
    settings.format = strformat
    settings.output_path = output_name
    request = groupdocs_conversion_cloud.ConvertDocumentRequest(settings)
    response = convert_api.convert_document(request)
    print('Document converted successfully ' + str(response))
except groupdocs_conversion_cloud.ApiException as e:
    print("Exception when calling get_supported_conversion_types: {0}".format(e.message))