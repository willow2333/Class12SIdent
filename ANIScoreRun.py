from ANIScore import *

def run():
    # P =Path('/data/qinliu/Work/SCU_Forensic_class/Ref/AddRef')
    # refname = 'SecondId'

    parser = argparse.ArgumentParser()
    parser.add_argument("--refpath",help='The absolute path of reference.')
    parser.add_argument("--refname",help='The name of reference.')
    args = parser.parse_args()
    P = Path(args.refpath)
    refname = args.refname
    aniffle= 'output_ANI.txt'
    file = '{}.fasta'.format(refname)
    splitrefP = P/'{}.split'.format(file)
    ani = ANIScore()
    ani.PreAnalysis(P,file)
    # self.ANI(P,P/aniffle)
    ani.CdHit(P,refname)
    refclass = P/'{}_class.id.txt'.format(refname)
    dfrefclass = pd.read_csv(refclass,sep='\t')
    refclassDict = {}
    for k, v in dfrefclass.groupby('clusterid'):
        refclassDict[k] = v['Id'].tolist()
    ani.SnpRefClass(splitrefP,refclassDict,P,refname)
    
if __name__ == "__main__":
    run()