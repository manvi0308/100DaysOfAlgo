#include <string.h>
#include <stdio.h>
int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
        int n,c=0,m=0;
        scanf("%d",&n);
        while(n--)
        {
            int c1=0,c2=0;
            char s1[10],s2[10];
            scanf("%s %s",s1,s2);
            for(int i=0;i<strlen(s1);i++)
                c1=c1+(s1[i]-48);
            for(int i=0;i<strlen(s2);i++)
                c2=c2+(s2[i]-48);
             if(c1==c2)
            {
                c++;
                m++;
            }
            else if(c1>c2)
                c++;
            else
                m++;
        }
        if(c==m)
            printf("2 %d\n",c);
        else if(c>m)
            printf("0 %d\n",c);
        else
            printf("1 %d\n",m);
    }
    return 0;
