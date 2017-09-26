import junit.framework.TestCase
import org.junit.Assert._

/**
 * A JUnit test case class.
 * Every method starting with the word "test" will be called when running
 * the test with JUnit.
 */
class TmpTest(name: String) extends TestCase(name) {

  /** A test method.
    *  (Replace "X" with a name describing the test.  You may write as
    *  many "testSomething" methods in this class as you wish, and each
    *  one will be called when running JUnit over this class.)
    */
  def testX() {
    assertTrue(Ob.num0 == Num(Ob.c))
  }

  /** Sample test method which tests no program code. */
  def testNothing() {
    assertTrue("Dummy Test", true)
    println("TESTING Nothing")
  }
}
