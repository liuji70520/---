
import sys
import numpy as np
import pandas as pd  
def makeAA531Dict(AA531FileName):
    filename = AA531FileName
    df = pd.read_csv(filename, delimiter='\t', header=None, skiprows=1)
    AA531Dict = df.set_index(0).T.to_dict('list')#选取第一列作为索引，‘.T’转置，‘to_dict('list')’将其转换为字典。其中字典的值是一个列表，包含每一列的值
    return AA531Dict

def file2matrix(AASeqFileName,seqlength,AA531Dict):
    filename = AASeqFileName
    df = pd.read_csv(AASeqFileName,sep="\t",header=None)
    #得到行数numberOFlines，开辟内存数组returnMat，同时准备一个二维数组储存三肽数字标签Y
    numberOFlines = len(df)
    seqlength = seqlength
    returnMat = np.zeros((numberOFlines,seqlength*531))
    Y = np.zeros((numberOFlines,1))
    #遍历每个三肽，与字典比对，添加到一个新的列表中
    for lineNum in range(numberOFlines):
        Y[lineNum] = float(df.iloc[lineNum,1])
        feaVec = []
        for AA in df.iloc[lineNum,0]:
            if AA in AA531Dict.keys():
                feaVec.extend(AA531Dict[AA])
            else:
                print('Warning: nonregular amino acid found! Coding "%s" in "%s" (seqId: %d) with 531 zeros.' % (AA, AAseq, lineNum))
                feaVec.extend([0.0]*531)
                Y[lineNum] = -1
        returnMat[lineNum,:] = np.array(feaVec)
        lineNum += 1
    return Y,returnMat,lineNum
if __name__ == '__main__':
   AASeqFileName = sys.argv[1]
   AA531FileName = sys.argv[2]
   seqLength = int(sys.argv[3])
   outputFileName = sys.argv[4]
   AA531Dict = makeAA531Dict(AA531FileName)
   Y, AA531Mat, SeqNum = file2matrix(AASeqFileName, seqLength, AA531Dict)
   np.savetxt(outputFileName, np.hstack((Y, AA531Mat)), fmt='%g', delimiter='\t')
   print('The number of sequences is %d. Matrix of features is saved in %s' % (SeqNum, outputFileName))



