#! /bin/sh

#USER
api=$1
user='200'
password='200200123'
host=192.168.69.51



echo $api $user $password $host

echo "[USER1] /my/search/phonebook"
echo "[USER2GET] /my/phonebook"
echo "[USER2POST] /my/phonebook"
echo "[USER2DELETE] /my/phonebook"
echo "[USER3] /my/pagedphonebook?start={start-row}&end={end-row}"
echo "??[USER4GET] /my/phonebook/entry/{entryId}"
echo "??[USER4PUT] /my/phonebook/entry/{entryId}"
echo "??[USER4POST] /my/phonebook/entry/{entryId}"
echo "??[USER4DELETE] /my/phonebook/entry/{entryId}"
echo "??[USER5PUT] /my/phonebook/showContactsOnPhone/{value}"
echo "[USER6] /my/call/{to}"
echo "[USER7] /my/voicemail/pin/{pin}"
echo "[USER8] /my/voicemail/operator/{operator}"
echo "[USER9] /my/voicemail/operator/"
echo "[USER10GET] /my/forward"
echo "[USER10PUT] /my/forward"
echo "[USER11] /my/feed/voicemail/{folder}"
echo "[USER12GET] /my/contact-information"
echo "[USER12PUT] /my/contact-information"
echo "[USER13] /my/time"
echo "[USER14] /my/mailbox/{user}/preferences/activegreeting/{greeting}"
echo "[USER15] /my/conferences"
echo "[USER16] /my/conference/{confName}/{command}"
echo "[USER17] /my/activecdrs"
echo "[USER18] /my/logindetails"
echo "[USER19GET] /my/redirect/cdr/{user}?limit=maxrecs&fromdate=yyyymmdd"
echo "[USER19POST] /my/redirect/callcontroller/callingParty/calledParty"
echo "??[USER19PUT] /my/redirect/"
echo "??[USER19DELETE] /my/redirect/"
echo "[USER20] /my/conferencedetails/{confName}"
echo "[USER21] /my/phonebook/googleImport"
echo "[CDR1] /cdr/{user}?limit=maxrecs&fromdate=yyyymmdd"
echo "[CALLCTRL1] /callcontroller/callingParty/calledParty GET method"
echo "[CALLCTRL2] /callcontroller/callingParty/calledParty POST method"
echo "[ATT1] /auto-attendant"
echo "[ATT2] /auto-attendant/{attendant}/special PUT method"
echo "[ATT3] /auto-attendant/{attendant}/special DELETE method"
echo "[ATT4] /auto-attendant/specialmode GET method"
echo "[ATT5] /auto-attendant/specialmode PUT method"
echo "[ATT6] /auto-attendant/specialmode DELETE method"
echo "[PHONE1] /phone"
echo "[PHONE2] /phone/{serialNumber}/profile/{profile-file}"
echo "[PHONEBOOK1] /phonebook/{name}"
echo "[PHONEBOOK2] /phonebook"
echo "[PERM1] /permission"
echo "[PERM2] /permission/{name}"
echo "[PERM3] /user-group-permission"
echo "[PERM4] /user-group-permission/{id}"
echo "[PERM5] /user-permission"
echo "[PERM6] /user-permission/{id}"
echo "[OTHER1] /avatar/{user}"
echo "[OTHER2] /branch"
echo "[OTHER3] /branch/{id}"
echo "[OTHER4] /user-group"
echo "[OTHER5] /user-group/{id}"
echo "[OTHER6] /user"
echo "[OTHER7] /user/{id}"


if test $api = 'USER1'; then
    echo "Rtrieve delle info relative a uno specifico contatto (207 )nella rubrica dell'utente $user"
    echo curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/search/phonebook?query=207"
    curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/search/phonebook?query=207"
fi
if test $api = 'USER2GET'; then
    echo "Rtrieve dell'intera rubrica dell'utente $user"
    echo curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/phonebook"
    curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/phonebook"
fi
if test $api = 'USER2POST'; then
    echo "crea una rubrica dell'utente $user"
    echo curl --digest -k -X POST -d @user2post.xml -u $user:$password "http://$host/sipxconfig/rest/my/phonebook"
    curl --digest -k -X POST -d @user2post.xml -u $user:$password "http://$host/sipxconfig/rest/my/phonebook"
fi
if test $api = 'USER2DELETE'; then
    echo "Rtrieve dell'intera rubrica dell'utente $user"
    echo curl --digest -k -X DELETE -d @user2post.xml -u $user:$password "http://$host/sipxconfig/rest/my/phonebook"
    curl --digest -k -X DELETE -d @user2post.xml -u $user:$password "http://$host/sipxconfig/rest/my/phonebook"
fi
if test $api = 'USER3'; then
    echo "Retrieve dei contatti dell'utente 200 dalla start row (0) alla end row (2)"
    echo curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/pagedphonebook?start=0&end=2"
    curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/pagedphonebook?start=0&end=2"
fi
if test $api = 'USER4GET'; then
    echo "Rtrieve delle info relative a uno specifico contatto nella rubrica dell'utente 200 con una specifica entry id"
    echo curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/phonebook/entry/0"
    #curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/phonebook/entry/11"
fi
if test $api = 'USER4POST'; then
    echo "Rtrieve delle info relative a uno specifico contatto nella rubrica dell'utente 200 con una specifica entry id"
    echo curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/phonebook/entry/0"
    #curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/phonebook/entry/11"
fi
if test $api = 'USER4PUT'; then
    echo "Rtrieve delle info relative a uno specifico contatto nella rubrica dell'utente 200 con una specifica entry id"
    echo curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/phonebook/entry/0"
    #curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/phonebook/entry/11"
fi
if test $api = 'USER4DELETE'; then
    echo "Rtrieve delle info relative a uno specifico contatto nella rubrica dell'utente 200 con una specifica entry id"
    echo curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/phonebook/entry/0"
    #curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/phonebook/entry/11"
fi

if test $api = 'USER5PUT'; then
    echo "Modifica il flag per consentire la visualizzazione dei contatti su telefono"
    echo curl --digest -k -X PUT -u $user:$password "http://$host/sipxconfig/rest/my/phonebook/showContactsOnPhone/true"
    #curl --digest -k -X PUT -u $user:$password "http://$host/sipxconfig/rest/my/phonebook/showContactsOnPhone/true"
fi

if test $api = 'USER6'; then
    echo "Effettua una chiamata dall'utente 200 al 207"
    echo curl --digest -k -X PUT -u $user:$password "http://$host/sipxconfig/rest/my/call/207"
    curl --digest -k -X PUT -u $user:$password "http://$host/sipxconfig/rest/my/call/207"
fi
if test $api = 'USER7'; then
    echo "Effettua il cambio PIN per l'accesso alla Voicemail"
    echo curl --digest -k -X PUT -u $user:$password "http://$host/sipxconfig/rest/my/voicemail/pin/500"
    curl --digest -k -X PUT -u $user:$password "http://$host/sipxconfig/rest/my/voicemail/pin/500"
fi
if test $api = 'USER8'; then
    echo "Effetua la modifica dell'operatore (es.: una estensione) associato alla casella vocale"
    echo curl --digest -k -X PUT -u $user:$password "http://$host/sipxconfig/rest/my/voicemail/operator/{operator}"
    curl --digest -k -X PUT -u $user:$password "http://$host/sipxconfig/rest/my/voicemail/operator/207"
fi
if test $api = 'USER9'; then
    echo "Recupera il varore dell'operatore configurato per il personal autoattendant"
    echo curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/voicemail/operator"
    curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/voicemail/operator"
fi

if test $api = 'USER10GET'; then
    echo "Recupera i dettagli relativi al Call forwarding dell'utente"
    echo curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/forward"
    curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/forward"
fi

if test $api = 'USER10PUT'; then
    echo "Recupera i dettagli relativi al Call forwarding dell'utente"
    echo curl --digest -k -X PUT -d @user10put.xml -u $user:$password "http://$host/sipxconfig/rest/my/forward"
    curl --digest -k -X PUT -d @user10put.xml -u $user:$password "http://$host/sipxconfig/rest/my/forward"
fi

if test $api = 'USER11'; then
    echo "Ritorna il contenuto di una specifica folder ella voicemail"
    echo curl --digest -k -X GET -u $user:$password "https://@$host/sipxconfig/rest/my/feed/voicemail/inbox"
    curl --digest -k -X GET -u $user:$password "https://$host/sipxconfig/rest/my/feed/voicemail/inbox"
fi

if test $api = 'USER12GET'; then
    echo "Recupera le informazioin dell'utente "
    echo curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/contact-information"
    curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/contact-information"
fi

if test $api = 'USER12PUT'; then
    echo "Imposta le informazioin dell'utente "
    echo curl --digest -k -X PUT -d @user12put.xml -u $user:$password "http://$host/sipxconfig/rest/my/contact-information"
    curl --digest -k -X PUT -d @user12put.xml -u $user:$password "http://$host/sipxconfig/rest/my/contact-information"
fi

if test $api = 'USER13'; then
    echo "Recupera data e ora del server host"
    echo curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/time"
    curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/time"
fi
if test $api = 'USER14'; then
    echo "Imposta il tipo di messaggio per la voicemail "
    echo curl --digest -k -X PUT -u $user:$password "http://$host/sipxconfig/rest/my/mailbox/$user/preferences/activegreeting/standard"
    curl --digest -k -X PUT -u $user:$password "http://$host/sipxconfig/rest/my/mailbox/$user/preferences/activegreeting/standard"
fi
if test $api = 'USER15'; then
    echo "elenca tutte le conferenze associate all'utente"
    echo curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/conferences"
    curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/conferences"
fi
if test $api = 'USER16'; then
    echo "esegue un comando per la conferenza dell'utente"
    echo curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/conference/test/"
    curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/conference/test/lock"
fi
if test $api = 'USER17'; then
    echo "mostra i dettagli sulle chiamate attive dell'utente"
    echo curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/activecdrs"
    curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/activecdrs"
fi
if test $api = 'USER18'; then
    echo "Mostra i dettagli delle login dell'utente: UserName, imId .."
    echo curl --digest -k -X GET -u $user:$password "https://$host/sipxconfig/rest/my/logindetails"
    curl --digest -k -X GET -u $user:$password "https://$host/sipxconfig/rest/my/logindetails"
fi

if test $api = 'USER19GET'; then
    echo "api usata per fare redirect su un'altra url per callcontroller mailbox  o media"
    echo curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/redirect/cdr/$user?limit=10&fromdate=20121101"
    curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/redirect/cdr/$user?limit=10&fromdate=20121101"
fi

if test $api = 'USER19POST'; then
    echo "api usata per fare redirect su un'altra url per callcontroller mailbox  o media"
    echo curl --digest -k -X POST -u $user:$password "http://$host/sipxconfig/rest/my/redirect/callcontroller/203/207"
    curl --digest -k -X POST -u $user:$password "http://$host/sipxconfig/rest/my/redirect/callcontroller/203/207"
fi

if test $api = 'USER19PUT'; then
    echo "api usata per fare redirect su un'altra url per callcontroller mailbox  o media"
    echo curl --digest -k -X PUT -u $user:$password "http://$host/sipxconfig/rest/my/redirect/"
    #curl --digest -k -X PUT -u $user:$password "http://$host/sipxconfig/rest/my/redirect"
fi

if test $api = 'USER19DELETE'; then
    echo "api usata per fare redirect su un'altra url per callcontroller mailbox  o media"
    echo curl --digest -k -X DELETE -u $user:$password "http://$host/sipxconfig/rest/my/redirect"
    #curl --digest -k -X DLETE -u $user:$password "http://$host/sipxconfig/rest/my/redirect"
fi

if test $api = 'USER20'; then
    echo "restituisce tutti i parametri della conferenza attiva"
    echo curl --digest -k -X GET -u $user:$password "http://$host/sipxconfig/rest/my/conferencedetails/test"
    curl --digest -k -X GET -u $user:$password "https://$host/sipxconfig/rest/my/conferencedetails/test"
fi

if test $api = 'USER21'; then
    echo "Import contacts from google"
    echo curl --digest -k -X POST -u $user:$password "http://$host/sipxconfig/rest/my/phonebook/googleImport"
    curl --digest -k -X POST -d user21.xml -u $user:$password "http://$host/sipxconfig/rest/my/phonebook/googleImport"
fi

#CDR & CALLCONTROLLER
if test $api = 'CDR1'; then
    echo "Retrieve dei CDR per l'utente nel periodo specificato"
    echo curl --digest -k -X GET -u $user:$password "http://$host:6666/cdr/$user?limit=10&fromdate=20121101"
    curl --digest -k -X GET -u $user:$password "http://$host:6666/cdr/$user?fromdate=20121101&limit=2"
fi

if test $api = 'CALLCTRL1'; then
    echo ""
    echo curl --digest -k -X GET -u $user:$password "http://$host:6666/callcontroller/$user/201"
    curl -k --digest -X GET -u $user:$password "http://$host:6666/callcontroller/$user/201"
fi

if test $api = 'CALLCTRL2'; then
    echo ""
    echo curl --digest -k -X POST -u $user:$password "http://$host:6666/callcontroller/$user/203?agent=$user&sipMethod=INVITE"
    curl --digest -k -X POST -u $user:$password "http://$host:6666/callcontroller/$users/203?agent=$user&sipMethod=INVITE"
fi


# AutoAttendant
if test $api = 'ATT1'; then
    echo "elenca tutti gli autorisponditori settati in Opsip"
    echo curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/auto-attendant"
    curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/auto-attendant"
fi

if test $api = 'ATT2'; then
    echo "Imposta l'attendant specificato come special attendant da usare" 
    echo curl --digest -k -X PUT -u superadmin:superadmin "http://$host/sipxconfig/rest/auto-attendant/operator/special"
    curl --digest -k -X PUT -u superadmin:superadmin "http://$host/sipxconfig/rest/auto-attendant/operator/special"
fi

if test $api = 'ATT3'; then
    echo "Ripulisce il valore del parametro dell'attendant specificato come special attendant da usare" 
    echo curl --digest -k -X DELETE -u superadmin:superadmin "http://$host/sipxconfig/rest/auto-attendant/operator/special"
    curl --digest -k -X DELETE -u superadmin:superadmin "http://$host/sipxconfig/rest/auto-attendant/operator/special"
fi

if test $api = 'ATT4'; then
    echo "Restituisce il valore del flag specialmode per autoattendant"
    echo curl --digest -k -X GET "https://$user:$password@$host/sipxconfig/rest/my/phonebook/googleImport"
    curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/auto-attendant/specialmode"
fi

if test $api = 'ATT5'; then
    echo "Imposta il valore del flag specialmode per autoattendant a true"
    echo curl --digest -k -X PUT "http://$host/sipxconfig/rest/auto-attendant/specialmode"
    curl --digest -k -X PUT -u superadmin:superadmin "http://$host/sipxconfig/rest/auto-attendant/specialmode"
fi

if test $api = 'ATT6'; then
    echo "Imposta il valore del flag specialmode per autoattendant a false"
    echo curl --digest -k -X DELETE "http://$host/sipxconfig/rest/auto-attendant/specialmode"
    curl --digest -k -X DELETE -u superadmin:superadmin "http://$host/sipxconfig/rest/auto-attendant/specialmode"
fi


# Phone and Phonebook
if test $api = 'PHONE1'; then
    echo "Consente di creare un telefono utilizzando un file xml per definire SerialNumber model e description"
    echo     curl --digest -k -X POST -u superadmin:superadmin -d @phone.xml "http://$host/sipxconfig/rest/phone"
    curl --digest -k -X POST -u superadmin:superadmin -d @phone.xml "http://$host/sipxconfig/rest/phone"
fi

if test $api = 'PHONE2'; then
    echo "restituisce il profilo di un dato telefono presente in Opsip sulla base del suo serial number"
    echo curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/phone/000413292b5e/profile/000413292B5E.xml" 
    curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/phone/000413292b5e/profile/000413292B5E.xml" 
fi

if test $api = 'PHONEBOOK1'; then
    echo "Restutiuisce i contatti presenti in una specifica rubrica telefonica"
    echo curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/phonebook/PhoneBookProva"
    curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/phonebook/PhoneBookProva"
fi

if test $api = 'PHONEBOOK2'; then
    echo "Restituisce l'elenco di tutte le rubriche telefoniche in Opsip presenti nella sezione phonebooks"
    echo curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/phonebook"
    curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/phonebook"
fi


# Permissions
if test $api = 'PERM1'; then
    echo "Restituisce l'elenco di tutte le permission definite per i dialing plan"
    echo  curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/permission"
    curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/permission"
fi

if test $api = 'PERM2'; then
    echo "Restituisce i dettagli di una specifica permission"
    echo curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/permission/900Dialing"
    curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/permission/900Dialing"
fi

if test $api = 'PERM3'; then
    echo "mostra lo stato delle permission per tutti gli user groups"
    echo curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/phonebook"
    curl --digest -k -X GET  -u superadmin:superadmin "http://$host/sipxconfig/rest/user-group-permission"
fi
if test $api = 'PERM4'; then
    echo "mostra lo stato delle permission per uno specifico user-group" 
    echo     curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/user-group-permission/4"
    curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/user-group-permission/4"
fi

if test $api = 'PERM5'; then
    echo "Restituisce l'elenco di le permission di ogni utente"
    echo curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/user-permission"
    curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/user-permission"
fi

if test $api = 'PERM6'; then
    echo "Restituisce l'elenco di le permission di un utente specifico"
    echo     curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/user-permission/11"
    curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/user-permission/11"
fi


# Other
if test $api = 'OTHER1'; then
    echo "Ritorna l'avatar dell'utente specificato"
    echo curl --digest -k -X GET -u superadmin:superadmin "https://$user:$password@$host/sipxconfig/rest/avatar/200"
    curl --digest -k -X GET -u superadmin:superadmin "https://$user:$password@$host/sipxconfig/rest/avatar/200"
fi
if test $api = 'OTHER2'; then
    echo "Restituisce l'elenco dei branch creati per una suddivisione di utenti gateway e server (utile in caso di dislocazione degli apparati o degli utenti)"
    echo    curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/branch"
    curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/branch"
fi
if test $api = 'OTHER3'; then
    echo "Restituisce un branch specifico esistente"
    echo  curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/branch/1"
    curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/branch/1"
fi
if test $api = 'OTHER4'; then
    echo "Restituisce l'elenco dei gruppi di utenti"
    echo    curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/user-group"
    curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/user-group"
fi
if test $api = 'OTHER5'; then
    echo "Restituisce i dettagli di uno specifico gruppo utenti"
    echo     curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/user-permission/11"
    curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/user-group/24"
fi
if test $api = 'OTHER6'; then
    echo "Restituisce i dettagli degli utenti di sistema. Pin e Password non sono mostrate"
    echo    curl --digest -k -X GET  -u superadmin:superadmin "http://$host/sipxconfig/rest/user"
    curl --digest -k -X GET  -u superadmin:superadmin "http://$host/sipxconfig/rest/user"
fi
if test $api = 'OTHER7'; then
    echo "Restituisce i dettagli di uno specifico utente del sistema. Pin e Password non sono mostrate"
    echo    curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/user/10"
    curl --digest -k -X GET -u superadmin:superadmin "http://$host/sipxconfig/rest/user/10"
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


