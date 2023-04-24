# -*- coding:UTF-8 -*-
import streamlit as st
import pandas as pd

def main():
    st.title("Hello World")

    # text
    st.text('This is so {}'.format("good"))

    # Header
    st.header('This is Header')

    # subheader
    st.subheader('This is subHeader')

    # Markdown
    st.markdown('## This is Markdown')

    # 색상이 들어간 텍스트 feature
    st.success('성공')
    st.warning('경고')
    st.info('정보롸 관련된 탭')
    st.error('에러 메세지')
    st.exception('예외처리')

    # st.write()
    st.write('일반텍스트')
    st.write(1+2)
    st.write(dir(str))

    st.title(':sunglasses:')

    # help
    st.help(range)
    st.help(st.title)

    # 데이터 불러오기
    iris = pd.read_csv('data/iris.csv')

    st.title("IRIS 테이블")
    st.dataframe(iris, 200,100) # Height, Width

    st.title('table()')
    st.write(iris)

if __name__ == '__main__':
    main()