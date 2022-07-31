import os
from antlr4 import *
from ParserLexer import ParserLexer
from ParserParser import ParserParser
from ParserVisitor import ParserVisitor

def main():
    data = FileStream("test.cl")
    lexer = ParserLexer(data)
    stream = CommonTokenStream(lexer)
    parser = ParserParser(stream)
    tree = parser.program()

    # Errores semanticos
    visitor = MyVisitor()
    visitor.visit(tree)
    
    #Arbol
    os.system('grun Parser program test.cl -gui -tokens')

class MyVisitor(ParserVisitor):
    def visitProgram(self, ctx):
        print("program")
        return self.visitChildren(ctx)
    
    def visitFeature(self, ctx:ParserParser.FeatureContext):
        print("feature")

        return self.visitChildren(ctx)

    def visitStringExpr(self, ctx:ParserParser.StringExprContext):
        if (len(ctx.getText()) > 10):
            print("ERROR: Longitud de string excedida\n\tLinea [%s:%s] %s" % (ctx.start.line, ctx.start.column, ctx.getText()))

        return self.visitChildren(ctx)

if __name__ == "__main__":
    main()