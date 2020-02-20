export class Triangle {
  constructor(...sides) {
    [this.a, this.b, this.c] = sides.sort();
    if (this.a + this.b <= this.c) {
      throw new Error("Side lengths do not correspond to a triangle.");
    }
  }

  isEquilateral() {
    return this.a == this.c;
  }

  isIsosceles() {
    return this.a == this.b || this.b == this.c;
  }

  isScalene() {
    return this.a < this.b && this.b < this.c;
  }
}
