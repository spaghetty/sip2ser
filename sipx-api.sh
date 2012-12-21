#! /bin/sh

#USER
api=$1
user='208'
password='208208123'
host=192.168.69.51



echo $api $user $password $host

echo "[USER1] /my/search/phonebook"
echo "[USER2] /my/phonebook"
echo "[USER3] /my/pagedphonebook?start={start-row}&amp;end={end-row}"
echo "[USER4] /my/phonebook/entry/{entryId}"
echo "[USER5] /my/phonebook/showContactsOnPhone/{value}"
echo "[USER6] /my/phonebook/googleImport"
echo "[USER7] /my/call/{to}"
echo "[USER8] /my/voicemail/pin/{pin}"
echo "[USER9] /my/voicemail/operator/{operator}"
echo "[USER10] /my/voicemail/operator/"
echo "[USER11] /my/forward"
echo "[USER12] /my/feed/voicemail/{folder}"
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/my/contact-information
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/my/time
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/my/mailbox/{user}/preferences/activegreeting/{greeting}
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/my/conferences
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/my/conference/{confName}/{command}
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/my/activecdrs
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/my/logindetails
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/my/redirect
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/my/conferencedetails/{confName}


if test $api = 'USER1'; then
    echo "Rtrieve delle info relative a uno specifico contatto (207 )nella rubrica dell'utente 200"
    echo curl --digest -k -X GET "http://$user:$password@$host/sipxconfig/rest/my/search/phonebook?query=207"
    curl --digest -k -X GET "http://$user:$password@$host/sipxconfig/rest/my/search/phonebook?query=207"
fi
if test $api = 'USER2'; then
    echo "Rtrieve dell'intera rubrica dell'utente 200"
    echo curl --digest -k -X GET "http://$user:$password@$host/sipxconfig/rest/my/phonebook"
    curl --digest -k -X GET "http://$user:$password@$host/sipxconfig/rest/my/phonebook"
fi
if test $api = 'USER3'; then
    echo "Retrieve dei contatti dell'utente 200 dalla start row (0) alla end row (2)"
    echo curl --digest -k -X GET "http://$user:$password@$host/sipxconfig/rest/my/pagedphonebook?start=0&end=2"
    curl --digest -k -X GET "http://$user:$password@$host/sipxconfig/rest/my/pagedphonebook?start=0&end=2"
fi
if test $api = 'USER4'; then
    echo "Rtrieve delle info relative a uno specifico contatto nella rubrica dell'utente 200 con una specifica entry id"
    echo curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/my/phonebook/entry/0"
    #curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/my/phonebook/entry/0"
    echo "To be reviewed...entry filter not working"
fi
if test $api = 'USER5'; then
    echo "Modifica il flag per consentire la visualizzazione dei contatti su telefono"
    echo curl --digest -k -X PUT "http://$user:$password@$host/sipxconfig/rest/my/phonebook/showContactsOnPhone/true"
    #curl --digest -k -X GET "http://$user:$password@$host/sipxconfig/rest/my/phonebook/showContactsOnPhone/1"
    echo "To be reviewed..."
fi
if test $api = 'USER6'; then
    echo "Import contacts from google"
    echo curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/my/phonebook/googleImport"
    #curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/my/phonebook/googleImport"
    echo "To be reviewed..."
fi
if test $api = 'USER7'; then
    echo "Effettua una chiamata dall'utente 200 al 207"
    echo curl --digest -k -X PUT "http://$user:$password@$host/sipxconfig/rest/my/call/207"
    curl --digest -k -X PUT "http://$user:$password@$host/sipxconfig/rest/my/call/207"
fi
if test $api = 'USER8'; then
    echo "Effettua il cambio PIN per l'accesso alla Voicemail"
    echo curl --digest -k -X PUT "https://$user:$password@$host/sipxconfig/rest/my/voicemail/pin/500"
    curl --digest -k -X PUT "http://$user:$password@$host/sipxconfig/rest/my/voicemail/pin/500"
fi
if test $api = 'USER9'; then
    echo "Effetua la modifica dell'operatore (es.: una estensione) associato alla casella vocale"
    echo curl --digest -k -X GET "http://$user:$password@$host/sipxconfig/rest/my/voicemail/operator/{operator}"
    curl --digest -k -X GET "http://$user:$password@$host/sipxconfig/rest/my/voicemail/operator/207"
fi
if test $api = 'USER10'; then
    curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/my/phonebook"
fi
if test $api = 'USER11'; then
    curl --digest -k -X GET "http://$user:$password@$host/sipxconfig/rest/my/search/phonebook?query=207"
fi
if test $api = 'USER12'; then
    curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/my/phonebook"
fi
if test $api = 'USER13'; then
    curl --digest -k -X GET "http://$user:$password@$host/sipxconfig/rest/my/search/phonebook?query=207"
fi
if test $api = 'USER14'; then
    curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/my/phonebook"
fi
if test $api = 'USER115'; then
    curl --digest -k -X GET "http://$user:$password@$host/sipxconfig/rest/my/search/phonebook?query=207"
fi
if test $api = 'USER16'; then
    curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/my/phonebook"
fi
if test $api = 'USER17'; then
    curl --digest -k -X GET "http://$user:$password@$host/sipxconfig/rest/my/search/phonebook?query=207"
fi
if test $api = 'USER18'; then
    curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/my/phonebook"
fi
if test $api = 'USER19'; then
    curl --digest -k -X GET "http://$user:$password@$host/sipxconfig/rest/my/search/phonebook?query=207"
fi
if test $api = 'USER20'; then
    curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/my/phonebook"
fi
if test $api = 'USER21'; then
    curl --digest -k -X GET "http://$user:$password@$host/sipxconfig/rest/my/search/phonebook?query=207"
fi



# OpenACD
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/openacd-agent-group
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/openacd-agent-group/{id}
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/openacd-skill
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/openacd-skill/{id}
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/openacd-skill-group
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/openacd-skill-group/{id}
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/openacd-client
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/openacd-client/{id}
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/openacd-queue-group
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/openacd-queue-group/{id}
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/openacd-release-code
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/openacd-release-code/{id}
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/openacd-queue
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/openacd-queue/{id}
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/openacd-agent
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/openacd-agent/{id}
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/openacd-line
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/openacd-setting
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/openacd-line/{id}
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/openacd-dial-string
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/openacd-dial-string/{id}


# AutoAttendant
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/auto-attendant
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/auto-attendant/{attendant}/special
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/auto-attendant/specialmode


# Phone and Phonebook
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/phone
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/phonebook/{name}
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/phonebook
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/phone/{serialNumber}/profile/{name}

# Permissions
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/permission
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/permission/{name}
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/user-group-permission
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/user-group-permission/{id}
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/user-permission
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/user-permission/{id}

# Others
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/avatar/{user}
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/branch
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/branch/{id}
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/user-group
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/user-group/{id}
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/user
# % >> curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/user/{id}
