package com.company.Algorithms.G;

import java.util.Random;


//Main class
public class Genetic {

    Individual fittest, fittest2;
    Population population = new Population();

    int generationCount = 0;


    public static void main(String[] args) {

        Random random = new Random();
        Genetic genetic = new Genetic();

        //Initialize population
        genetic.population.initializePopulation(10);

        //Calculate fitness of each individual
        genetic.population.calculateFitness();

        System.out.println("Generation" + genetic.generationCount + " Fittest: " + genetic.population.fittest);

        //While population gets an individual with maximum fitness
        while (genetic.population.fittest < 5) {
            ++genetic.generationCount;

            //Do selection
            genetic.selection();

            //Do crossover
            genetic.crossover();

            //Do mutation under a random probability
            if (random.nextInt() % 7 < 5) {
                genetic.mutation();
            }

            //Add fittest offspring to population
            genetic.addFittestOffspring();

            //Calculate new fitness value
            genetic.population.calculateFitness();

            System.out.println("Generation " + genetic.generationCount + " Fittest: " + genetic.population.fittest);
        }

        System.out.println("\nSolution found in generation " + genetic.generationCount);
        System.out.println("Fitness: " + genetic.population.getBest().fitness);
        System.out.print("Genes: ");
        for (int i = 0; i < 5; i++) {
            System.out.print(genetic.population.getBest().genes[i]);
        }

        System.out.println("");

    }

    /**
     * Selection
     */
    void selection() {

        //Select the most fittest individual
        fittest = population.getBest();

        //Select the second most fittest individual
        fittest2 = population.getSecondFittest();
    }

    /**
     * Crossover
     */
    void crossover() {
        Random random = new Random();

        //Select a random crossover point
        int crossOverPoint = random.nextInt(population.individuals[0].GLength);

        //Swap values among parents
        for (int i = 0; i < crossOverPoint; i++) {
            int temp = fittest.genes[i];
            fittest.genes[i] = fittest2.genes[i];
            fittest2.genes[i] = temp;

        }

    }

    /**
     * Mutation
     */
    void mutation() {
        Random random = new Random();

        //Select a random mutation point
        int mutationPoint = random.nextInt(population.individuals[0].GLength);

        //Flip values at the mutation point
        if (fittest.genes[mutationPoint] == 0) {
            fittest.genes[mutationPoint] = 1;
        } else {
            fittest.genes[mutationPoint] = 0;
        }

        mutationPoint = random.nextInt(population.individuals[0].GLength);

        if (fittest2.genes[mutationPoint] == 0) {
            fittest2.genes[mutationPoint] = 1;
        } else {
            fittest2.genes[mutationPoint] = 0;
        }
    }

    //Get fittest offspring
    Individual getFittestOffspring() {
        if (fittest.fitness > fittest2.fitness) {
            return fittest;
        }
        return fittest2;
    }


    //Replace least fittest individual from most fittest offspring
    void addFittestOffspring() {

        //Update fitness values of offspring
        fittest.findFitness();
        fittest2.findFitness();

        //Get index of least fit individual
        int leastFittestIndex = population.getLeastFittestIndex();

        //Replace least fittest individual from most fittest offspring
        population.individuals[leastFittestIndex] = getFittestOffspring();
    }

}


/**
 * Individual class
 */
class Individual {

    int fitness = 0;
    int[] genes = new int[5];
    int GLength = 5;

    public Individual() {
        Random random = new Random();

        //Set genes randomly for each individual
        for (int i = 0; i < genes.length; i++) {
            genes[i] = Math.abs(random.nextInt() % 2);
        }

        fitness = 0;
    }

    //Calculate fitness
    public void findFitness() {

        fitness = 0;
        //GLength = 5;
        for (int i = 0; i < GLength; i++) {
            if (genes[i] == 1) {
                ++fitness;
            }
        }
    }

}

/**
 * Population class
 */
class Population {


    Individual[] individuals = new Individual[10];
    int fittest = 0;
    int PSize = 10;

    //Initialize population
    public void initializePopulation(int PSize) {
        for (int i = 0; i < individuals.length; i++) {
            individuals[i] = new Individual();
        }
    }

    //reach the best and fittest individual
    public Individual getBest() {
        int maxFit = Integer.MIN_VALUE;
        int maxFitIndex = 0;
        for (int i = 0; i < individuals.length; i++) {
            if (maxFit <= individuals[i].fitness) {
                maxFit = individuals[i].fitness;
                maxFitIndex = i;
            }
        }
        fittest = individuals[maxFitIndex].fitness;
        return individuals[maxFitIndex];
    }

    //Get the second  fittest individual
    public Individual getSecondFittest() {
        int maxFit1 = 0;
        int maxFit2 = 0;
        for (int i = 0; i < individuals.length; i++) {
            if (individuals[i].fitness > individuals[maxFit1].fitness) {
                maxFit2 = maxFit1;
                maxFit1 = i;
            } else if (individuals[i].fitness > individuals[maxFit2].fitness) {
                maxFit2 = i;
            }
        }
        return individuals[maxFit2];
    }

    //Get index of least fittest individual
    public int getLeastFittestIndex() {
        int minFitVal = Integer.MAX_VALUE;
        int minFitIndex = 0;
        for (int i = 0; i < individuals.length; i++) {
            if (minFitVal >= individuals[i].fitness) {
                minFitVal = individuals[i].fitness;
                minFitIndex = i;
            }
        }
        return minFitIndex;
    }

    //Calculate fitness of each individual
    public void calculateFitness() {

        for (int i = 0; i < individuals.length; i++) {
            individuals[i].findFitness();
        }
        getBest();
    }

}

