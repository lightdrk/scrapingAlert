import time
import argparse
from helper.telegram import sendMessage
from helper.file import createFile
from colorama import Fore
from helper.webScrap.eventtim import eventtim
from helper.webScrap.fansale import websiteFansale
from helper.webScrap.kleinanzeigen import websiteklein
from helper.webScrap.willhaben import websiteWill


def diffBetween(a, aa, b, bb):
    if a == b and aa == bb:
        return []

    if aa != bb or a != b:
        return list(set(aa) - set(bb))



if __name__ == '__main__':
    usage= '''
        USAGE:-
        You can use ScrapingAlert to monitor different websites by specifying command-line arguments. Here are the available options:

        --all: Monitor all supported websites.
        --e: Monitor the Eventim website.
        --f: Monitor the Fansale website.
        --k: Monitor the Kleinanzeigen website.
        --w: Monitor the Willhaben website.
        --new: Create credentials.

        Example: python main.py --[all,e,f,k,w] [tag name].

    '''
    parser = argparse.ArgumentParser(prog="ScrapAlter", usage=usage)

    parser.add_argument('--all',help="using tag for all website")
    parser.add_argument('--e',help="tag for eventtim website")
    parser.add_argument('--f', help=" using tag for fansale website")
    parser.add_argument('--k', help="using tag for kleinanzeigen website")
    parser.add_argument('--w', help="using tag for willhaben website")
    parser.add_argument('--new', help="creating creds")

    args = parser.parse_args()

    try:

        if args.new:
            createFile(args.new)


        if args.all:
            diff_eventtim = eventtim(args.all)
            diff_fansale = websiteFansale(args.all)
            [kleinanzeigen_number, kleinanzeigen_list] = websiteklein(args.all)
            [willhaben_number, willhaben_list] = websiteWill(args.all)

            while True:
                new_dif_eventtim = eventtim(args.all)
                new_diff_fansale = websiteFansale(args.all)
                [new_kleinanzeigen_number, new_kleinanzeigen_list] = websiteklein(args.all)
                [new_willhaben_number, new_willhaben_list] = websiteWill(args.all)
                
                if dif_eventtim != new_dif_eventtim:
                    sendMessage("website: eventtim changes")
                    print('updated')

                if diff_fansale != new_diff_fansale:
                    fansale_number, fansale_list = new_fansale_number, new_fansale_list
                    sendMessage("wensite: fansale", str(fdiff))

                kdiff = diffBetween(new_kleinanzeigen_number, new_kleinanzeigen_list, kleinanzeigen_number, kleinanzeigen_list)
                if len(kdiff):
                    kleinanzeigen_number, kleinanzeigen_list = new_kleinanzeigen_number, new_kleinanzeigen_list
                    sendMessage("website: kleinanzeigen", str(kdiff))

                wdiff = diffBetween(new_willhaben_number, new_willhaben_list,willhaben_number, willhaben_list)
                if len(wdiff):
                    willhaben_number, willhaben_list = new_willhaben_number, new_willhaben_list
                    sendMessage("website: willhaben", str(wdiff))

                time.sleep(20)
        if args.e:
            diff_eventtim = eventtim(args.e)

        if args.f:
            diff_fansale = websiteFansale(args.f)

        if args.k:
            [kleinanzeigen_number, kleinanzeigen_list] = websiteklein(args.k)

        if args.w:
            [willhaben_number, willhaben_list] = websiteWill(args.w)

        while args.e or args.f or args.k or args.w:
            if args.e:
                new_diff_eventtim = eventtim(args.e)
                if diff_eventtim != new_diff_eventtim :
                    sendMessage("website: eventtim changes")
                    print('updated')

            if args.f:
                new_diff_fansale = websiteFansale(args.f)

                if new_diff_fansale != diff_fansale:
                    fansale_number, fansale_list = new_fansale_number, new_fansale_list
                    sendMessage("wensite: fansale \n available")


            if args.k:
                [new_kleinanzeigen_number, new_kleinanzeigen_list] = websiteklein(args.k)

                kdiff = diffBetween(new_kleinanzeigen_number, new_kleinanzeigen_list, kleinanzeigen_number, kleinanzeigen_list)
                if len(kdiff):
                    kleinanzeigen_number, kleinanzeigen_list = new_kleinanzeigen_number, new_kleinanzeigen_list
                    sendMessage("website: kleinanzeigen", str(kdiff))

            if args.w:
                [new_willhaben_number, new_willhaben_list] = websiteWill(args.w)

                wdiff = diffBetween(new_willhaben_number, new_willhaben_list,willhaben_number, willhaben_list)
                if len(wdiff):
                    willhaben_number, willhaben_list = new_willhaben_number, new_willhaben_list
                    sendMessage("website: willhaben", str(wdiff))

            time.sleep(20)
    except KeyboardInterrupt:
        print(Fore.RED+'\nexited ....')
