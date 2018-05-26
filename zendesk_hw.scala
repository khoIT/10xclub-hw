/*
Write a simple cipher that will take a string and replace each letter in the range a-z with the corresponding character n steps along the alphabet, for example: if n=13

The character 'a' should be replaced with 'n'
The character 'r' should be replaced with 'e'
Sample acceptance criteria:

'hello world' => 'uryyb jbeyq'
'zendesk, beautifully simple.' => 'mraqrfx, ornhgvshyyl fvzcyr.'
*/

object Solution extends App {
  def transform(c: Byte, distance: Int): Char = c match {
    case 32 => ' '
    case 44 => ','
    case 46 => '.'
    case c if c + distance > 122 => (c + distance - 26).toChar
    case c if c + distance < 96 => (c + distance + 26).toChar
    case _ => (c + distance).toChar
  }

  def cipher(decodedString: String, cipher: Int): String = {
    val res = decodedString.map(c => transform(c.toByte, cipher))
    return res
  }
  println(cipher("hello world", 13))
  println(cipher("zendesk, beautifully simple.", 13))
  println(cipher("hello world", -1))
}
