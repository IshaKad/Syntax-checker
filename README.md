**Python-Based C Syntax Checker**



A Python-based syntax checker for C programs that analyzes source code through lexical analysis, parsing, Abstract Syntax Tree (AST) generation, and symbol table management.



The project demonstrates the core concepts behind compiler construction by breaking down a C source program into manageable stages and reporting syntax errors.



**Features**



Lexical Analysis: Identifies tokens in the C source code.



Syntax Analysis: Checks whether the token sequence follows the supported grammar rules.



Abstract Syntax Tree (AST): Represents the syntactic structure of the source program using AST nodes.



AST Printing: Displays the generated syntax tree in a readable format.



Symbol Table Management: Maintains information about identifiers encountered during analysis.



Error Handling: Reports errors encountered during lexical and syntax analysis.



Sample Input: Includes a C source file for testing the syntax checker.



**Project Structure**



syntax-checker/

├── ast\_nodes.py       # AST node definitions

├── ast\_printer.py     # AST display utilities

├── errors.py          # Error handling

├── lexer.py           # Lexical analysis

├── main.py            # Program entry point

├── parser.py          # Syntax analysis

├── symbol\_table.py    # Symbol table management

├── sample.c           # Sample C input program

├── requirements.txt   # Python dependencies

├── .gitignore         # Files excluded from Git

└── README.md          # Project documentation



Parser-generated files such as parsetab.py and parser.out may be created when the parser runs, depending on its configuration.



**Technologies Used**



Python — Core implementation



PLY (Python Lex-Yacc) — Lexical analysis and parsing, if configured in the project dependencies



C — Input language being analyzed



Git and GitHub — Version control and project hosting



**Getting Started**



**Prerequisites**



Python 3.11 or a compatible version



pip package manager



Installation



Clone the repository:



git clone https://github.com/IshaKad/syntax-checker.git

cd syntax-checker



Install the dependencies:



pip install -r requirements.txt



**Running the Project**



Run the main program:



python main.py



The program's input and output behavior depends on the implementation in main.py. Use sample.c as the sample source program if the application is configured to read that file.



**How It Works**



The syntax checker is organized into several components:



Lexical Analysis: The lexer scans source code and identifies tokens such as keywords, identifiers, operators, and punctuation.



Parsing: The parser processes tokens according to the grammar rules implemented in the project.



AST Construction: AST nodes represent the syntactic structure of the parsed program.



AST Visualization: The AST printer formats the tree for easier inspection.



Symbol Table: The symbol table stores identifier-related information maintained by the implementation.



Error Reporting: The error-handling component helps report invalid tokens or syntax that violates the supported grammar.



**Scope and Limitations**



This project focuses on the subset of C syntax implemented in its lexer and parser. It should not be considered a complete C compiler or a replacement for a standards-compliant C compiler. The language constructs supported depend on the grammar and semantic checks implemented in the project.



**Future Improvements**



Expand grammar coverage for additional C language constructs.



Improve error messages with source-line and column information.



Add semantic checks for declarations, scopes, and identifier usage.



Develop automated test cases for valid and invalid programs.



Add AST visualization and structured diagnostic output.

