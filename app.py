 
import streamlit as st
import pickle
pickle_in=open('classifier.pkl','rb')
clf=pickle.load(pickle_in)
a=st.number_input('sepal length(cm)')
b=st.number_input('sepal width(cm)')
c=st.number_input('sepal length(cm)')
d=st.number_input('sepal width(cm)')
r=''
if st.button('PREDICT'):
  result=clf.predict([[a,b,c,d]]).squeeze()
  if result==0:
    st.success('SETOSA')
  elif result==0:
      st.success('VERSICOLOR')
  else:
    st.success('VIRGINCA')
      
