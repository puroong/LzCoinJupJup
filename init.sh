#!/bin/bash

#set username for lezhin login
if [$LZCOINJUPJUP_USERNAME = ""]
then
    echo "레진코믹스 로그인에 사용할 이메일을 입력하세요:"
    read LZCOINJUPJUP_USERNAME
    export LZCOINJUPJUP_USERNAME=$LZCOINJUPJUP_USERNAME
else
    echo "LZCOINJUPJUP_USERNAME already set: $LZCOINJUPJUP_USERNAME"
fi

#set password for lezhin login
if [$LZCOINJUPJUP_PASSWORD = ""]
then
    echo "레진코믹스 로그인에 사용할 비밀번호를 입력하세요:"
    read LZCOINJUPJUP_PASSWORD
    export LZCOINJUPJUP_PASSWORD=$LZCOINJUPJUP_PASSWORD
else
    echo "LZCOINJUPJUP_PASSWORD already set: $LZCOINJUPJUP_PASSWORD"
fi

#set login method for lezhin comics
if [$LZCOINJUPJUP_LOGIN_METHOD = ""]
then
    echo "레진코믹스 로그인 방법을 입력하세요(general, naver, facebook  중 하나):"
    read LZCOINJUPJUP_LOGIN_METHOD
    export LZCOINJUPJUP_LOGIN_METHOD=$LZCOINJUPJUP_LOGIN_METHOD
else
    echo "LZCOINJUPJUP_LOGIN_METHOD already set: $LZCOINJUPJUP_LOGIN_METHOD"
fi

#set username for facebook authentication
if [$LZCOINJUPJUP_FB_USERNAME = ""]
then
    echo "페이스북 이메일을 입력하세요:"
    read LZCOINJUPJUP_FB_USERNAME
    export LZCOINJUPJUP_FB_USERNAME=$LZCOINJUPJUP_FB_USERNAME
else
    echo "FACEBOOK_UESRNAME already set: $LZCOINJUPJUP_FB_USERNAME"
fi

#set password for facebook authentication
if [$LZCOINJUPJUP_FB_PASSWORD = ""]
then
    echo "페이스북 비밀번호를 입력하세요:"
    read LZCOINJUPJUP_FB_PASSWORD
    export LZCOINJUPJUP_FB_PASSWORD=$LZCOINJUPJUP_FB_PASSWORD
else
    echo "LZCOINJUPJUP_FB_PASSWORD already set: $LZCOINJUPJUP_FB_PASSWORD"
fi

#set username for twitter
if [$LZCOINJUPJUP_TT_USERNAME = ""]
then
    echo "트위터 이메일을 입력하세요:"
    read LZCOINJUPJUP_TT_USERNAME
    export TWTTER_USERNAME=$TWTTER_USERNAME
else
    echo "LZCOINJUPJUP_TT_USERNAME already set: $LZCOINJUPJUP_TT_USERNAME"
fi

#set password for twtter
if [$LZCOINJUPJUP_TT_PASSWORD = ""]
then
    echo "트위터 비밀번호를 입력하세요:"
    read LZCOINJUPJUP_TT_PASSWORD
    export LZCOINJUPJUP_TT_PASSWORD=$LZCOINJUPJUP_TT_PASSWORD
else
    echo "TWTTER_PASSWORD already set: $LZCOINJUPJUP_TT_PASSWORD"
fi
