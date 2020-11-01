# Question 5

st = []
ans = []

indar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
bellar = [221, 198, 203, 214, 213, 219, 220, 216, 218, 222]

for i in range(indar.size) :
    if st.size == 0 :
        st.append(bellar[i])
        ans.append('*')
        continue
    else :
        while bellar[i] > st[st.size-1] :
            st.pop()
        else :
            if st[st.size-2] == '*' :
                ans.append(1)
            else :
                ans.append([st.size-2]+1)
            st.append(bellar[i])
