from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
import pandas as pd
# from elasticsearch import Elasticsearch
app = Flask(__name__)
api = Api(app)

@app.route('/')
def getDashboard():
    return render_template('index.html', gson = {'name':'rajesh', 'age':24})

@app.route('/topics')
def getTopics():
    return render_template('topics.html')

@app.route('/search')
def getSearchPage():
    return render_template('search.html')

@app.route('/duplicate-search')
def getDuplicateSearchPage():
    return render_template('duplicate-search.html')
# class docifysearch(Resource):

#     def get(self,search_string):
#         es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
#         #data = pd.read_csv('users.csv')
#         #data=data[data.name.str.contains(ename)]
#         #data = data.to_dict('records')
#         ###########################################
#         flname=[]
#         text=[]
#         location=[]
#         #es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
#         query_body = {'size':10000,
#             "query": {
#                 "match": {
#                     "cleaned_text": search_string
#                     }
#                     }
#                     }
#         res=es.search(index='docify_ocr_out',body=query_body)
#         ht=res['hits']
#         for i in range(len(ht['hits'])):

#             text.append(ht['hits'][i]['_source']['cleaned_text'])
#             flname.append(ht['hits'][i]['_source']['file_name'])
#             location.append(ht['hits'][i]['_source']['filename_with_location'])

#         df=pd.DataFrame({'File Name':flname,'Summary':text,'Location':location})
#         df_search=df.copy()

#         df=df.to_dict('records')

#         query_body_ss = {'size':10000,"query": {"match_all": {}}}

#         res_ss=es.search(index='docify_similarity_scores',body=query_body_ss)

#         df_ss = pd.json_normalize(res_ss['hits']['hits'])
#         df_search.rename(columns={'File Name':'_source.file_name'},inplace=True)

#         merged=pd.merge(df_search[['_source.file_name']],df_ss[['_source.file','_source.file_name','_source.value']],left_on='_source.file_name',right_on='_source.file',how='left')
#         ssFiles=merged[merged['_source.value']>=0.7]
#         ssFiles=ssFiles.iloc[:,1:]
#         resDict=dict()
#         for i in ssFiles['_source.file'].unique():
#             ss_list=list(ssFiles[ssFiles['_source.file']==i]['_source.file_name_y'].values.flatten())
#             ss_list.remove(i)

#             resDict.update({i:ss_list})



#         return {'data' : df,'similarFiles':resDict}, 200


#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('name', required=True)
#         parser.add_argument('age', required=True)
#         parser.add_argument('city', required=True)
#         args = parser.parse_args()

#         data = pd.read_csv('users.csv')

#         new_data = pd.DataFrame({
#             'name'      : [args['name']],
#             'age'       : [args['age']],
#             'city'      : [args['city']]
#         })

#         data = data.append(new_data, ignore_index = True)
#         data.to_csv('users.csv', index=False)
#         return {'data' : new_data.to_dict('records')}, 201

#     def delete(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('name', required=True)
#         args = parser.parse_args()

#         data = pd.read_csv('users.csv')

#         data = data[data['name'] != args['name']]

#         data.to_csv('users.csv', index=False)
#         return {'message' : 'Record deleted successfully.'}, 200

# api.add_resource(docifysearch, '/docifysearch/<search_string>',endpoint='docifysearch')

# # Add URL endpoints
# #@app.route('/getCount',methods=['GET'])
# class fileGroupCount(Resource):
#     def get(self):
#         es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
#         query_body = {'size':10000,"query": {"match_all": {}}}

#         res=es.search(index='docify_metadata',body=query_body)
#         df = pd.json_normalize(res['hits']['hits'])
#         totalFiles=df.shape[0]
#         fileGroupCount=pd.pivot_table(data=df,index="_source.file_group",values="_index",aggfunc='count')
#         fileGroupCount=fileGroupCount.rename(columns={'_index':'FileGroup'}).to_dict()


#         fileTypeCount=pd.pivot_table(data=df,index="_source.file_type",values="_index",aggfunc='count')

#         fileTypeCount=fileTypeCount.rename(columns={'_index':'FileType'}).to_dict()
#         fileSize=pd.pivot_table(data=df,index="_source.file_type",values="_source.file_size",aggfunc='sum')

#         fileSize=fileSize.rename(columns={'_source.file_size':'FileType'}).to_dict()
#         ss_query_body = {'size':10000,"query": {"match_all": {}}}

#         res_ss=es.search(index='docify_similarity_scores',body=ss_query_body)

#         df_ss = pd.json_normalize(res_ss['hits']['hits'])

#         dup_no=df_ss[df_ss['_source.value']==1]['_source.file'].unique().size
#         percentageDuplicate=round(dup_no*100/totalFiles,2)



#         #data = pd.read_csv('users.csv')
#         #data=data[data.name.str.contains(ename)]
#         #data = data.to_dict('records')
#         return {"TotalFiles":totalFiles,"DuplicateFileNo":dup_no,"percentageDuplicate":percentageDuplicate,"GroupCount":fileGroupCount,"TypeCount":fileTypeCount,"FileSize":fileSize}, 200
# api.add_resource(fileGroupCount, '/fgc',endpoint='fgc')

# ############# Similar fileSize
# class similarFiles(Resource):
#     def get(self):
#         es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

#         ss_query_body = {'size':10000,"query": {"match_all": {}}}

#         res_ss=es.search(index='docify_similarity_scores',body=ss_query_body)

#         df_ss = pd.json_normalize(res_ss['hits']['hits'])

#         ss=df_ss[['_source.file','_source.file_name','_source.value']]
#         ss=ss.to_dict('records')



#         #data = pd.read_csv('users.csv')
#         #data=data[data.name.str.contains(ename)]
#         #data = data.to_dict('records')
#         return {"Similar Files":ss}, 200
# api.add_resource(similarFiles, '/sf',endpoint='sf')




if __name__ == '__main__':
    app.run(port="3000",debug=True)
