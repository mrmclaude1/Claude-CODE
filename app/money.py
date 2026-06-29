"""Money helpers. All currency math uses Decimal — never float — to avoid
rounding errors on dollar figures that appear on legal payment documents."""

from __future__ import annotations

from decimal import Decimal, ROUND_HALF_UP, InvalidOperation

CENTS = Decimal("0.01")


def money(value) -> Decimal:
    """Coerce a number/str to a Decimal rounded to cents (ROUND_HALF_UP).

    Accepts int, float, str, or Decimal. Rejects junk loudly rather than
    silently producing a wrong dollar amount.
    """
    if isinstance(value, Decimal):
        d = value
    else:
        try:
            # Route through str so float artifacts (0.1) don't leak in.
            d = Decimal(str(value))
        except (InvalidOperation, TypeError, ValueError) as exc:
            raise ValueError(f"Not a valid monetary amount: {value!r}") from exc
    return d.quantize(CENTS, rounding=ROUND_HALF_UP)


def pct(value) -> Decimal:
    """Coerce a percentage to a Decimal fraction.

    Accepts 0.10 or 10 (interpreted as 10%) — anything > 1 is treated as a
    whole-number percent and divided by 100. Below or equal to 1 is a fraction.
    """
    try:
        d = Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError) as exc:
        raise ValueError(f"Not a valid percentage: {value!r}") from exc
    if d > 1:
        d = d / Decimal("100")
    if d < 0 or d > 1:
        raise ValueError(f"Percentage out of range [0,1]: {value!r}")
    return d


def fmt(value: Decimal) -> str:
    """Format a Decimal as a $ string with thousands separators."""
    return f"${money(value):,.2f}"
