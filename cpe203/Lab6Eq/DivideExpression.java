class DivideExpression
        extends BinaryExpression
{

   public DivideExpression(final Expression lft, final Expression rht)
   {
      super(lft, rht, "/");
   }

   protected double _applyOperator(final double lft, final double rht) {
      return lft / rht;
   }
}

