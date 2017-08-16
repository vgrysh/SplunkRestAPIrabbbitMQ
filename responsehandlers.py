#add your custom response handler class to this module
import json
import datetime

#the default handler , does nothing , just passes the raw output directly to STDOUT
class DefaultResponseHandler:
    
    def __init__(self,**args):
        pass
        
    def __call__(self, response_object,raw_response_output,response_type,req_args,endpoint):
        cookies = response_object.cookies
        if cookies:
            req_args["cookies"] = cookies        
        print_xml_stream(raw_response_output)
          
#template
class MyResponseHandler:
    
    def __init__(self,**args):
        pass
        
    def __call__(self, response_object,raw_response_output,response_type,req_args,endpoint):        
        print_xml_stream("foobar")

'''various example handlers follow'''

class RMQEventHandler:

    def __init__(self,**args):
        pass

    def __call__(self, response_object,raw_response_output,response_type,req_args,endpoint):
        if response_type == "json":
            output = json.loads(raw_response_output)
            print_xml_stream(json.dumps(output["object_totals"]))
            print_xml_stream(json.dumps(output["message_stats"]))
        else:
            print_xml_stream(raw_response_output)

#HELPER FUNCTIONS
    
# prints XML stream
def print_xml_stream(s):
    print "<stream><event unbroken=\"1\"><data>%s</data><done/></event></stream>" % encodeXMLText(s)


def encodeXMLText(text):
    text = text.replace("&", "&amp;")
    text = text.replace("\"", "&quot;")
    text = text.replace("'", "&apos;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    text = text.replace("\n", "")
    return text