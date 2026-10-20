import java.io.File;
import java.io.FileNotFoundException; // Import this class to handle errors
import java.util.Scanner;

class Relation {

// This method returns if matrix is reflexive or not
public static Boolean isReflexive(int mat[][],int n){
for(int i=0;i<n;i++){
if(mat[i][i]!=1)
return false;
}
return true;
}

// This method returns if matrix is antireflexive or not
public static Boolean isAntiReflexive(int mat[][],int n){
for(int i=0;i<n;i++){
if(mat[i][i]!=0)
return false;
}
return true;
}

// This method returns if matrix is symmetric or not
public static Boolean isSymmetric(int mat[][],int n){
for(int i=0;i<n;i++){
for(int j=0;j<n;j++){
if(i==j)
continue;
if(mat[i][j]!=mat[j][i])
return false;
}
}
return true;
}

// This method returns if matrix is antisymmetric or not
public static Boolean isAntiSymmetric(int mat[][],int n){
for(int i=0;i<n;i++){
for(int j=0;j<n;j++){
if(i==j)
continue;
if(mat[i][j]==mat[j][i])
return false;
}
}
return true;
}

public static void main(String[] args) {

// Reading file name from user
System.out.print("File input: ");
Scanner sc = new Scanner(System.in);
String file_name = sc.nextLine();
sc.close();
// try to open and read file
try {
File myObj = new File(file_name);
Scanner myReader = new Scanner(myObj);
int mat[][] = new int[10][10];
int i=0;
// reading the file and filling mat
while (myReader.hasNextLine()) {
String data = myReader.nextLine();
for(int j=0;j<10;j++){
mat[i][j] = Integer.parseInt(data.split(" ")[j]);
}
i++;
}
// Displaying all the output
System.out.println("Reflexive - " + (isReflexive(mat, 10) ? "yes" : "no"));
System.out.println("AntiReflexive - " + (isAntiReflexive(mat, 10) ? "yes" : "no"));
System.out.println("Symmetric - " + (isSymmetric(mat, 10) ? "yes" : "no"));
System.out.println("Antisymmetric - " + (isAntiSymmetric(mat, 10) ? "yes" : "no"));
myReader.close();
} catch (FileNotFoundException e) { // if error occurred while opening the file
System.out.println("An error occurred.");
e.printStackTrace();
}
}
}
