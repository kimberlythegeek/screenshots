### Localization for Server-side strings of Firefox Screenshots
### Please don't localize Firefox, Firefox Screenshots, or Screenshots


## Global phrases shared across pages, prefixed with 'g'

gMyShots = Omat kaappaukset
gHomeLink = Etusivu
gNoShots =
    .alt = Kaappauksia ei löytynyt
gScreenshotsDescription = Kuvakaappaukset helposti. Ota, tallenna ja jaa kuvakaappauksia poistumatta Firefoxista.

## Header

buttonSettings =
    .title = Asetukset
buttonSignIn =
    .title = Kirjaudu sisään
screenshotsLogo =
    .title = Screenshots-etusivu
bannerMessage = Kirjaudu tai rekisteröidy, niin voit käyttää kaappauksiasi kaikilta laitteiltasi ja tallentaa suosikkisi ikuisesti.
bannerUpsell = { gScreenshotsDescription } <a>Hanki Firefox nyt</a>

## Footer

# Note: link text for a link to mozilla.org
footerLinkMozilla = Mozilla
footerLinkTerms = Käyttöehdot
footerLinkPrivacy = Tietosuojakäytäntö
footerReportShot = Ilmoita kaappaus
    .title = Ilmoita tämä kaappaus väärinkäytön, roskauksen tai muun ongelman takia
footerLinkFaqs = UKK
footerLinkDMCA = Ilmoita immateriaalioikeuksien loukkauksesta
footerLinkDiscourse = Anna palautetta
footerLinkRemoveAllData = Poista kaikki tiedot

## Creating page

# Note: { $title } is a placeholder for the title of the web page
# captured in the screenshot. The default, for pages without titles, is
# creatingPageTitleDefault.
creatingPageTitle = Luodaan: { $title }
creatingPageTitleDefault = sivu
creatingPageWaitMessage = Tallennetaan kaappausta…

## Home page

homePageDescription =
    .content = Kuvien kaappaminen intuitiivisesti, suoraan selaimessasi. Kaappaa, tallenna ja jaa kuvakaappauksia selatessasi verkkoa Firefoxilla.
homePageButtonMyShots = Siirry omiin kaappauksiini
homePageTeaser = Tulossa pian…
homePageDownloadFirefoxTitle = Firefox
homePageDownloadFirefoxSubTitle = Lataa ilmaiseksi
# Note: do not translate 'Firefox Screenshots' when translating this string
homePageHowScreenshotsWorks = Miten Firefox Screenshots toimii
homePageGetStartedTitle = Aloitetaan
# Note: Screenshots is an abbreviation for Firefox Screenshots, and should not be translated.
homePageGetStartedDescription = Huomaa uusi Screenshots-kuvake työkalupalkissa. Valitse se, niin Screenshots-valikko avautuu selainikkunan päälle.
# Note: Screenshots is an abbreviation for Firefox Screenshots, and should not be translated.
homePageGetStartedDescriptionPageAction = Valitse Screenshots-kuvake osoitepalkissa olevasta Sivun toiminnot -valikosta, niin Screenshots-valikko avautuu selainikkunan päälle.
homePageCaptureRegion = Kaappaa alue
# Note: Screenshots is an abbreviation for Firefox Screenshots, and should not be translated.
homePageCaptureRegionDescription = Valitse kaapattava alue napsauttamalla ja vetämällä. Tai pidä hiirtä sen päällä ja napsauta – Screenshots valitsee alueen puolestasi. PIdätkö näkemästäsi? Valitse Tallenna, niin voit katsella kuvakaappaustasi verkossa, tai alas osoittava nuoli, niin voit ladata sen tietokoneellesi.
homePageCapturePage = Kaappaa sivu
homePageCapturePageDescription = Kaappaa kokonaisia sivuja käyttämällä yläoikean kulman painikkeita. Tallenna näkyvä alue -painike kaappaa alueen, jonka voit nähdä vierittämättä sivua, ja Tallenna koko sivu -painike tallentaa kaiken sivulla olevan.
homePageSaveShare = Tallenna ja jaa
homePageLegalLink = Lakiteksti
homePagePrivacyLink = Tietosuoja
homePageTermsLink = Käyttöehdot
homePageCookiesLink = Evästeet

## Leave Screenshots page

leavePageRemoveAllData = Poista kaikki tiedot
# Note: do not translate 'Firefox Screenshots' when translating this string
leavePageErrorAddonRequired = Tilin poistamiseksi Firefox Screenshots pitää olla asennettuna
leavePageErrorGeneric = Tapahtui virhe
# Note: do not translate 'Firefox Screenshots' when translating this string
leavePageWarning = Tämä poistaa kaikki Firefox Screenshots -palvelun tietosi pysyvästi.
leavePageButtonProceed = Jatka
leavePageButtonCancel = Peruuta
leavePageDeleted = Kaikki kuvakaappauksesi on poistettu!

## Not Found page

notFoundPageTitle = Sivua ei löydy
notFoundPageIntro = Oho.
notFoundPageDescription = Sivua ei löydy.

## Shot page

# This is the HTML title tag of the page
shotPageTitle = Kuvakaappaus: { $originalTitle }
shotPageAlertErrorUpdatingExpirationTime = Vanhentumisen tallennus epäonnistui
shotPageAlertErrorDeletingShot = Kaappauksen poisto epäonnistui
shotPageAlertErrorUpdatingTitle = Nimen tallennus epäonnistui
shotPageConfirmDelete = Haluatko varmasti poistaa tämän kaappauksen pysyvästi?
shotPageShareButton =
    .title = Jaa
shotPageCopyButton =
    .title = Kopioi kuva leikepöydälle
shotPageCopied = Kopioitu
shotPageShareFacebook =
    .title = Jaa Facebookissa
shotPageShareTwitter =
    .title = Jaa Twitterissä
shotPageSharePinterest =
    .title = Jaa Pinterestissä
shotPageShareEmail =
    .title = Jaa linkki sähköpostitse
shotPageShareLink = Saa jaettava linkki tähän kaappaukseen:
shotPagePrivacyMessage = Kaikki linkin haltijat voivat katsoa tätä kaappausta.
shotPageCopyImageText =
    .label = Kopioi kuvateksti
shotPageConfirmDeletion = Haluatko varmasti poistaa tämän kaappauksen pysyvästi?
# Note: <timediff></timediff> is a placeholder for a future relative time clause like 'in 3 days' or 'tomorrow'
shotPageTimeExpirationMessage = Jos et tee mitään, kaappaus poistetaan pysyvästi <timediff></timediff>.
# Note: { $date } is a placeholder for a localized future date as returned by Date.toLocaleString.
# For example, in en-US, { $date } could be "7/12/2017, 1:52:50 PM".
shotPageRestoreButton = palauta { $date } saakka
shotPageExpiredMessage = Tämä kaappaus on vanhentunut.
# Note: This phrase is followed by an empty line, then the URL of the source page
shotPageExpiredMessageDetails = Tässä on sivu, josta kaappaus alun perin luotiin:
shotPageDeleteButton =
    .title = Poista tämä kaappaus
shotPageDownloadShot =
    .title = Lataa
shotPageEditButton =
    .title = Muokkaa tätä kuvaa
shotPagefavoriteButton =
    .title = Merkitse tämä kaappaus suosikiksi
shotPageBackToHomeButton =
    .title = Etusivu
shotPageAllShotsButton =
    .title = Kaikki kaappaukset
shotPageScreenshotsDescription = Kuvakaappaukset helposti. Ota, tallenna ja jaa kuvakaappauksia poistumatta Firefoxista.
shotPageDMCAMessage = Tämä kaappaus ei ole enää saatavissa, koska kolmas osapuoli teki immateriaalioikeusvaatimuksen.
# Note: { $dmca } is a placeholder for a link to send email (a 'mailto' link)
shotPageDMCAContact = Pyydä lisätietoja lähettämällä sähköpostia osoitteeseen { $dmca }.
# Note: do not translate 'Firefox Screenshots' when translating this string
shotPageDMCAWarning = Jos kaappauksiisi kohdistuu useita vaatimuksia, voimme perua käyttöoikeutesi Firefox Screenshots -palveluun.
# Note: { $url } is a placeholder for a shot page URL
shotPageDMCAIncludeLink = Liitä sähköpostiisi tämän kaappauksen verkko-osoite: { $url }
shotPageKeepFor = Kuinka kauan tämä kaappaus tulisi säilyttää?
# Note: shotPageSelectTime is a placeholder label for the time selection dropdown.
shotPageSelectTime = Valitse aika
# The ∞ is used to indicate that the shot won't expire. It is also used in
# shotIndexNoExpirationSymbol. Try to use the same symbol in both strings, or
# if no such symbol is available for a language/culture, simply leave it out.
shotPageKeepIndefinitelyWithSymbol = Toistaiseksi ∞
shotPageKeepTenMinutes = 10 minuuttia
shotPageKeepOneHour = 1 tunti
shotPageKeepOneDay = 1 päivä
shotPageKeepOneWeek = 1 viikko
shotPageKeepTwoWeeks = 2 viikkoa
shotPageKeepOneMonth = 1 kuukausi
shotPageSaveExpiration = tallenna
shotPageCancelExpiration = peruuta
shotPageDoesNotExpire = ei vanhene
# Note: <timediff></timediff> is a placeholder for a future relative time clause, like "in 1 week" or "tomorrow"
shotPageTimeExpiresIn = vanhenee <timediff></timediff>
# Note: <timediff></timediff> is a placeholder for a past relative time clause, like "1 week ago" or "yesterday"
shotPageTimeExpired = vanheni <timediff></timediff>
timeDiffJustNow = juuri nyt
timeDiffMinutesAgo =
    { $number ->
        [one] 1 minuutti sitten
       *[other] { $number } minuuttia sitten
    }
timeDiffHoursAgo =
    { $number ->
        [one] 1 tunti sitten
       *[other] { $number } tuntia sitten
    }
timeDiffDaysAgo =
    { $number ->
        [one] eilen
       *[other] { $number } päivää sitten
    }
timeDiffFutureSeconds = muutaman sekunnin kuluttua
timeDiffFutureMinutes =
    { $number ->
        [one] 1 minuutin kuluttua
       *[other] { $number } minuutin kuluttua
    }
timeDiffFutureHours =
    { $number ->
        [one] 1 tunnin kuluttua
       *[other] { $number } tunnin kuluttua
    }
timeDiffFutureDays =
    { $number ->
        [one] huomenna
       *[other] { $number } päivän kuluttua
    }
errorThirdPartyCookiesEnabled = Jos otit tämän kaappauksen etkä pysty poistamaan sitä, voit joutua sallimaan kolmannen osapuolen evästeet väliaikaisesti selaimen asetuksista.

## Shot Page New Feature Promotion Dialog.

# Note: If possible, choose a short translation to better fit into the card.
promoTitle = Huomio!
promoMessage = Päivitetyillä muokkaustyökaluilla voit rajata ja korostaa kuvaasi sekä lisätä tekstiä.
promoLink = Kokeile niitä
promoCloseButton =
    .title = Sulje ilmoitus

## Annotations

annotationPenButton =
    .title = Kynä
annotationHighlighterButton =
    .title = Korostus
annotationUndoButton =
    .title = Kumoa
annotationRedoButton =
    .title = Tee uudelleen
annotationTextButton =
    .title = Lisää tekstiä
# Note: This button reverts all the changes on the image since the start of the editing session.
annotationClearButton =
    .title = Pyyhi
annotationCropButton =
    .title = Rajaa
annotationSaveEditButton = Tallenna
    .title = Tallenna muokkaus
annotationCancelEditButton = Peruuta
    .title = Peruuta muokkaus
annotationCropConfirmButton = Vahvista
    .title = Vahvista valinta
annotationCropCancelButton = Peruuta
    .title = Peruuta valinta
annotationColorWhite =
    .title = Valkoinen
annotationColorBlack =
    .title = Musta
annotationColorRed =
    .title = Punainen
annotationColorGreen =
    .title = Vihreä
annotationColorBlue =
    .title = Sininen
annotationColorYellow =
    .title = Keltainen
annotationColorPurple =
    .title = Violetti
annotationColorSeaGreen =
    .title = Merenvihreä
annotationColorGrey =
    .title = Harmaa
# Note: annotationTextSize is a title for text size selection dropdown.
annotationTextSize =
    .title = Tekstin koko
# Values shown in text size selection dropdown
textSizeSmall = Pieni
textSizeMedium = Keskikokoinen
textSizeLarge = Suuri
# Confirm and Cancel button title shown when using text tool
textToolConfirmButton = Vahvista
    .title = Vahvista
textToolCancelButton = Peruuta
    .title = Peruuta
# Default placeholder used in input field when adding text annotations
textToolInputPlaceholder =
    .placeholder = Hei

## The following are the title and message for an error displayed as a Firefox
## notification. It is triggered by an action in the shot page and the strings
## are passed from the shot page to the addon.

copyImageErrorTitle = Jokin meni pieleen
copyImageErrorMessage = Kuvakaappausta ei voitu kopioida leikepöydälle.

## Settings Page

settingsDisconnectButton = Katkaise yhteys
    .title = Katkaise yhteys
settingsGuestAccountMessage = Vierastili
settingsSignInInvite = Voit synkronoida tiedot laitteiden välillä kirjautumalla sisään
settingsSignInButton = Kirjaudu sisään
    .title = Kirjaudu sisään
SettingsPageHeader = Firefox Screenshots -asetukset
settingsDescription = Voit kirjautua sisään Firefox-tilille ja synkronoida kaikki kaappauksesi laitteiden välillä ja katsella niitä yksityisesti.
settingsPageSubHeader = Synkronointi ja tilit
settingsClosePreferences =
    .title = Sulje asetukset

## Shotindex page

# { $status } is a placeholder for an HTTP status code, like '500'.
# { $statusText } is a text description of the status code, like 'Internal server error'.
shotIndexPageErrorDeletingShot = Kaappauksen poisto epäonnistui: { $status } { $statusText }
# { $searchTerm } is a placeholder for text the user typed into the search box
shotIndexPageSearchResultsTitle = Omat kaappaukset: haku sanoilla { $searchTerm }
# { $error } is a placeholder for a non-translated error message that could be shared
# with developers when debugging an error.
shotIndexPageErrorRendering = Sivun näyttäminen epäonnistui: { $error }
shotIndexPageSearchPlaceholder =
    .placeholder = Hae kaappauksista
shotIndexPageNoShotsMessage = Ei tallennettuja kaappauksia.
shotIndexPageNoShotsInvitation = Ryhdytäänpä luomaan sellaisia.
shotIndexPageLookingForShots = Etsitään kaappauksia…
shotIndexPageNoSearchResultsIntro = Hmm
shotIndexPageNoSearchResults = Haulla ei löytynyt yhtään kaappausta.
shotIndexPageMyShotsButton =
    .title = Omat kaappaukset
shotIndexPageClearSearchButton =
    .title = Tyhjennä haku
shotIndexPageConfirmShotDelete = Poistetaanko tämä kaappaus?
shotIndexPagePreviousPage =
    .title = Edellinen sivu
shotIndexPageNextPage =
    .title = Seuraava sivu
# This is tooltip for a "blank heart" symbol used in the upper top corner of the card for a shot on the
# My Shots page to indicate that the shot does expire.
shotIndexNonFavoriteIcon =
    .title = Tämä ei ole suosikkikaappaus, se vanhenee
# This is the tooltip for a "heart" symbol in the upper top corner of the
# card for a shot on the My Shots page. It indicate that the shot was marked as
# a favorite by the owner.
shotIndexFavoriteIcon =
    .title = Tämä on suosikkikaappaus eikä vanhene
shotIndexSyncedShot =
    .title = Kuvakaappaus otettu toisella laitteella

## Delete Confirmation Dialog

shotDeleteConfirmationMessage = Haluatko varmasti poistaa tämän kaappauksen?
shotDeleteCancel = Peruuta
    .title = Peruuta
shotDeleteConfirm = Poista
    .title = Poista

## Metrics page
## All metrics strings are optional for translation

# Note: 'Firefox Screenshots' should not be translated
metricsPageTitle = Firefox Screenshots Metrics
metricsPageTotalsQueryTitle = Totals
# Note: Screenshots is an abbreviation for Firefox Screenshots, and should not be translated.
metricsPageTotalsQueryDescription = An overview of Screenshots
metricsPageTotalsQueryDevices = Total devices registered
metricsPageTotalsQueryActiveShots = Active shots
metricsPageTotalsQueryExpiredShots = Expired (but recoverable)
metricsPageTotalsQueryExpiredDeletedShots = Expired (and deleted)
metricsPageShotsQueryTitle = Shots by Day
metricsPageShotsQueryDescription = Number of shots created each day (for the last 30 days)
metricsPageShotsQueryCount = Number of shots
metricsPageShotsQueryDay = Day
metricsPageUsersQueryTitle = Users by Day
metricsPageUsersQueryDescription = Number of users who created at least one shot, by day (last 30 days)
metricsPageUsersQueryCount = Number of users
metricsPageUsersQueryDay = Day
metricsPageUserShotsQueryTitle = Number of Shots per User
metricsPageUserShotsQueryDescription = The number of users who have about N total shots
metricsPageUserShotsQueryCount = Number of users
metricsPageUserShotsQueryShots = Approximate number of active (unexpired) shots
metricsPageRetentionQueryTitle = Retention by Week
metricsPageRetentionQueryDescription = Number of days from a userʼs first shot to most recent shot, grouped by starting week
metricsPageRetentionQueryUsers = Number of users
metricsPageRetentionQueryDays = Days from the userʼs first to most recent shot
metricsPageRetentionQueryFirstWeek = Week the user first created a shot
metricsPageTotalRetentionQueryTitle = Total Retention
metricsPageTotalRetentionQueryDescription = Length of time users have been creating shots, grouped by week
metricsPageTotalRetentionQueryUsers = Number of users
metricsPageTotalRetentionQueryDays = Days the user has been creating shots
metricsPageVersionQueryTitle = Add-on Version
metricsPageVersionQueryDescription = The version of the add-on used during login, in the last 14 days
metricsPageVersionQueryUsers = Number of users logging in
metricsPageVersionQueryVersion = Add-on version
metricsPageVersionQueryLastSeen = Day
metricsPageHeader = Metrics
# Note: { $created } is a placeholder for a localized date and time, like '4/21/2017, 3:40:04 AM'
metricsPageGeneratedDateTime = Generated at: { $created }
# Note { $time } is a placeholder for a number of milliseconds, like '100'
metricsPageDatabaseQueryTime = (database time: { $time }ms)
