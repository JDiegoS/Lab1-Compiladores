import os
from antlr4 import *
from ParserLexer import ParserLexer
from ParserListener import ParserListener
from ParserParser import ParserParser
from ParserVisitor import ParserVisitor

def main():
    data = FileStream("test2.cl")
    lexer = ParserLexer(data)
    stream = CommonTokenStream(lexer)
    parser = ParserParser(stream)
    tree = parser.program()

    #Arbol
    os.system('grun Parser program test2.cl -gui -tokens')

    # Tabla
    printer = ParserListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    # Errores semanticos
    visitor = MyVisitor()
    visitor.visit(tree)
    
    

class MyVisitor(ParserVisitor):    
    def visitAssignExpr(self, ctx:ParserParser.AssignExprContext):
        return self.visitChildren(ctx)

    def visitIdExpr(self, ctx:ParserParser.IdExprContext):
        return 'ID'

    def visitIntExpr(self, ctx:ParserParser.IntExprContext):
        return 'INT'
    
    def visitStringExpr(self, ctx:ParserParser.StringExprContext):
        if (len(ctx.getText()) > 10):
            print("ERROR: Longitud de string excedida\n\tLinea [%s:%s] %s" % (ctx.start.line, ctx.start.column, ctx.getText()))

        return 'STRING'
    
    def visitTrueExpr(self, ctx:ParserParser.TrueExprContext):
        return 'TRUE'
    
    def visitFalseExpr(self, ctx:ParserParser.TrueExprContext):
        return 'FALSE'
    
    def visitAddExpr(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        if (l != "INT" or r != "INT"):
            if l != "ID" and r != "ID":
                print("ERROR: No corresponden los tipos de la suma\n\tLinea [%s:%s] %s" % (ctx.start.line, ctx.start.column, ctx.getText()))


        #print(l)
        #print(r)
        #print(ctx.right.getText())
        #print(ctx.left.start)
        #print(ctx.left.start.type)
        return self.visitChildren(ctx)
    
    def visitMulExpr(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        if (l != "INT" or r != "INT"):
            if l != "ID" and r != "ID":
                print("ERROR: No corresponden los tipos de la multiplicacion\n\tLinea [%s:%s] %s" % (ctx.start.line, ctx.start.column, ctx.getText()))

        return self.visitChildren(ctx)
    
    def visitMinusExpr(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        if (l != "INT" or r != "INT"):
            if l != "ID" and r != "ID":
                print("ERROR: No corresponden los tipos de la resta\n\tLinea [%s:%s] %s" % (ctx.start.line, ctx.start.column, ctx.getText()))

        return self.visitChildren(ctx)
    
    def visitDivExpr(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)


        if (l != "INT" or r != "INT"):
            if l != "ID" and r != "ID":
                print("ERROR: No corresponden los tipos de la division\n\tLinea [%s:%s] %s" % (ctx.start.line, ctx.start.column, ctx.getText()))

        return self.visitChildren(ctx)
    
    def visitEqualsExpr(self, ctx:ParserParser.EqualsExprContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        if (l != r):
            if l != "ID" and r != "ID":
                print("ERROR: No corresponden los tipos de la comparacion <\n\tLinea [%s:%s] %s" % (ctx.start.line, ctx.start.column, ctx.getText()))

        return self.visitChildren(ctx)
    
    def visitLequalExpr(self, ctx:ParserParser.EqualsExprContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        if (l != r):
            if l != "ID" and r != "ID":
                print("ERROR: No corresponden los tipos de la comparacion <=\n\tLinea [%s:%s] %s" % (ctx.start.line, ctx.start.column, ctx.getText()))

        return self.visitChildren(ctx)

    def visitLtExpr(self, ctx:ParserParser.LtExprContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)
        

        if (l != r):
            if l != "ID" and r != "ID":
                print("ERROR: No corresponden los tipos de la comparacion =\n\tLinea [%s:%s] %s" % (ctx.start.line, ctx.start.column, ctx.getText()))

        return self.visitChildren(ctx)

    

if __name__ == "__main__":
    main()